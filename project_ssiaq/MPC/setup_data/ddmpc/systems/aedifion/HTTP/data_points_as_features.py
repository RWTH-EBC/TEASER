from ddmpc.systems.aedifion.HTTP.communication import *
from ddmpc.modeling.variables import *


class AedifionReadable(Readable, DataPoint):

    def __init__(
            self,
            name:       str,
            plt_opts:   PlotOptions,

            feedbackID: str,
            setPointID: Optional[str] = None,
            domain:     Optional[str] = DataPoint.default_domain,
            path:       Optional[str] = DataPoint.default_path,
            projectID:  Optional[int] = DataPoint.default_projectID,
            step:       Optional[bool] = False,
            offset:     float = 0,
    ):

        Readable.__init__(
            self,
            name=name,
            plt_opts=plt_opts,
            read_name=feedbackID,
        )

        DataPoint.__init__(
            self,
            feedbackID=feedbackID,
            setPointID=setPointID,
            domain=domain,
            path=path,
            projectID=projectID,
            step=step,
            offset=offset,
        )
