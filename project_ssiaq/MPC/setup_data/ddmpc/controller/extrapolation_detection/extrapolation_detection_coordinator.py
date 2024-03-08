from ddmpc.controller.extrapolation_detection.detector_trainer import DetectorTrainer
from ddmpc.modeling.process_models.main import Predictor
from ddmpc.controller.conventional import PID
from ddmpc.controller.model_predictive import NLPSolution
from ddmpc.utils.modes import *


class ExtrapolationDetectionCoordinator:

    writeNoveltyScores = False
    writeClfsInfo = False

    def __init__(
            self,
            base_controllers:       list[PID],
            detector_trainers:      dict[Predictor, DetectorTrainer],
            extrapolation_horizon:  int,
            weighting:              dict[Predictor, float] = None,
    ):
        self.detector_trainers = detector_trainers
        self.base_controllers = base_controllers
        self.extrapolation_horizon = extrapolation_horizon
        self.inExtrapolationMode = False

        if weighting is None:
            weighting = dict()
            for predictor in detector_trainers.keys():
                weighting[predictor] = 1
        self.weighting = weighting

    def validate_solution(self, nlp_solution: NLPSolution) -> tuple[dict, dict]:
        is_extrapolation, extrapolation_info = self.is_extrapolation(nlp_solution.inp_vals)
        extrapolation_info.update(self.get_clf_info())

        if not is_extrapolation:
            self.inExtrapolationMode = False
            extrapolation_info.update({'Extrapolation': False})
            return nlp_solution.optimal_controls, extrapolation_info

        print('Extrapolation detected.')
        self.inExtrapolationMode = True
        extrapolation_info.update({'Extrapolation': True})
        base_controls = self.get_base_controls()
        return base_controls, extrapolation_info

    def get_base_controls(self) -> dict:
        controls_dict = {}
        for base_controller in self.base_controllers:
            if not self.inExtrapolationMode:
                base_controller.reset()

            mpc_mode = base_controller.y.mode
            base_controller.y.mode = Steady
            base_controls, _ = base_controller()
            for key, value in base_controls.items():
                controls_dict.update({key: value})
            base_controller.y.mode = mpc_mode
        return controls_dict

    def is_extrapolation(self, predictor_inputs: dict) -> tuple[bool, dict]:
        extrapolation_sum = 0
        scores = dict()
        for predictor, inputs in predictor_inputs.items():
            for k in range(0, self.extrapolation_horizon):
                extrapolation_sum += \
                    self.weighting[predictor] * self.detector_trainers[predictor].detector.predict(inputs[k])
                if self.writeNoveltyScores:
                    scores[f'{predictor}_{k}_novelty'] = self.detector_trainers[predictor].detector.score(inputs[k])

        if extrapolation_sum / sum(self.weighting.values()) >= 0.5:
            return True, scores
        return False, scores

    def get_clf_info(self) -> dict:
        detector_info = dict()
        if self.writeClfsInfo:
            for predictor, detector_trainer in self.detector_trainers.items():
                for key, value in detector_trainer.info.values():
                    detector_info[predictor.__str__() + '_' + key] = value
        return detector_info
