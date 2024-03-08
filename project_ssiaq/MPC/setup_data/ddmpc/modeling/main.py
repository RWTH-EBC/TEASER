from ddmpc.modeling.variables import *
import ddmpc.utils.formatting as fmt


class Model:

    def __init__(self, *features: Feature):

        self.features = features

        self._sort()

        self._variable_mapping: dict[Variable, Feature] = dict()

        for f in self.features:
            self._variable_mapping[f.variable] = f

        self._validate()

    def __str__(self) -> str:
        return 'Model'

    def __repr__(self):
        return 'Model'

    def __getitem__(self, variable: Variable) -> Feature:
        """ Returns the Feature to the given Source """

        assert isinstance(variable, Variable), f'{variable} is not of type Source.'

        return self._variable_mapping[variable]

    def summary(self):

        print(f'{fmt.BOLD}Model Summary:{fmt.ENDC}')
        rows = [['Controlled  ', 'name', 'subs', 'mode']]

        for f in self.controlled:
            rows.append(['', f.variable.name, f.mode, f.variable.subs])

        rows.append([''])

        rows.append(['Controls    ', 'name', 'lb', 'ub', 'default', 'subs'])

        for f in self.controls:
            rows.append(['', f.variable.name, f.lb, f.ub, f.default, f.variable.subs])

        rows.append([''])

        rows.append(['Disturbances', 'name', 'subs', 'forecast_name'])

        for f in self.disturbances:
            rows.append(['', f.variable.name, f.forecast_name, f.variable.subs])

        rows.append([''])

        rows.append(['Connecting', 'name', 'subs'])

        for f in self.connecting:
            rows.append(['', f.variable.name, f.variable.subs])

        rows.append([''])

        rows.append(['Ignonred', 'name', 'subs'])

        for f in self.ignored:
            rows.append(['', f.variable.name, f.variable.subs])

        fmt.print_table(rows)

    def _sort(self):
        """ sorts the variables of the model in a way, that all subs are sorted after their parents """

        lst = list(self.features)
        n = len(lst)

        def iteration() -> bool:

            for i in range(n):

                f1: Feature = lst[i]

                for j in range(i + 1, n):

                    f2: Feature = lst[j]

                    if f2.variable in f1.variable.subs:

                        lst[i], lst[j] = lst[j], lst[i]
                        return True

            return False

        while iteration():
            pass

        self.features = tuple(lst)

    def _validate(self):
        """ Validates the model structure and completion """

        # check for only features
        for f in self.features:
            assert isinstance(f, Feature), f'{f} is not a Feature.'

        # checks for duplicates
        for i, f1 in enumerate(self.features):
            for j, f2 in enumerate(self.features[i+1:]):
                if f1 == f2:
                    raise ValueError(f'Duplicate found at position {i} and {i+j}! {f1, f2}, {self.features}')

        # sub feature check
        features_to_add = list()
        for feature in self.features:
            for sub in feature.variable.subs:
                if isinstance(self[sub], Tracking):
                    if isinstance(feature, Connection):

                        raise ValueError(f"{sub} cant be of type Tracking, when {feature} is not.")

                if sub not in [f.variable for f in self.features]:
                    if sub not in features_to_add:
                        features_to_add.append(sub)

        assert len(features_to_add) == 0, f'Please make sure to add these Features to the Model: {features_to_add}'

    @property
    def controlled(self) -> list[Controlled]:
        return [f for f in self.features if isinstance(f, Controlled)]

    @property
    def controls(self) -> list[Control]:
        return [f for f in self.features if isinstance(f, Control)]

    @property
    def disturbances(self) -> list[Disturbance]:
        return [f for f in self.features if isinstance(f, Disturbance)]

    @property
    def connecting(self) -> list[Connection]:
        return [f for f in self.features if isinstance(f, Connection)]

    @property
    def ignored(self) -> list[Tracking]:
        return [f for f in self.features if isinstance(f, Tracking)]

    @property
    def constructed(self) -> list[Constructed]:
        return [f.variable for f in self.features if isinstance(f.variable, Constructed)]

    @property
    def readable(self) -> list[Readable]:
        return [f.variable for f in self.features if isinstance(f.variable, Readable)]

    def update(self, idx: int, df: pd.DataFrame, inplace: bool = True) -> pd.DataFrame:

        for feature in self.features:

            df = feature.update(df=df, idx=idx, inplace=inplace)

        return df

    def process(self, df: pd.DataFrame, inplace: bool = True) -> pd.DataFrame:

        for feature in self.features:
            df = feature.process(df=df, inplace=inplace)

        return df


