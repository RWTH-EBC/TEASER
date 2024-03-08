import ddmpc.utils.formatting as fmt


class PlotOptions:

    def __init__(
            self,
            color:  list,
            line:   str,
            label:  str = None,
            second_axis: bool = False,
    ):
        """
        :param color:   Line color for the plotting
        :param line:    Line styles for the plotting
        :param label:   Label for the plotting
        """
        self.color: list = color
        self.line:  str = line
        self.label: str = label
        self.second_axis: bool = second_axis

    def __str__(self):
        return f'{self.__class__.__name__}(color={self.color}, line_style={self.line}, label={self.label})'

    def __repr__(self):
        return f'{self.__class__.__name__}(color={self.color}, line_style={self.line}, label={self.label})'


red_line = PlotOptions(color=fmt.red, line=fmt.line_solid)
light_red_line = PlotOptions(color=fmt.red, line=fmt.line_solid)
dark_red_line = PlotOptions(color=fmt.dark_red, line=fmt.line_solid)
blue_line = PlotOptions(color=fmt.blue, line=fmt.line_solid)
black_line = PlotOptions(color=fmt.black, line=fmt.line_solid)
light_grey_line = PlotOptions(color=fmt.light_grey, line=fmt.line_solid)
grey_line = PlotOptions(color=fmt.grey, line=fmt.line_solid)
dotted_grey_line = PlotOptions(color=fmt.grey, line=fmt.line_dotted)
dark_grey_line = PlotOptions(color=fmt.dark_grey, line=fmt.line_solid)
