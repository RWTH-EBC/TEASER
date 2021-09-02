import math
import pathlib
import numpy as np
import matplotlib.pyplot as plt
from ebcpy import TimeSeriesData
from os import walk


def main(with_plot=False):
    variables_building = ['ROM.intGainsConv.T', 'ROM.intGainsConv.Q_flow', 'ROM.intGainsRad.T', 'ROM.intGainsRad.Q_flow']
    zones = {'as Walls': 'blue', 'as Tabs': 'red'}
    basepath = pathlib.Path(__file__).parents[3].joinpath("Dymola_results")
    result_files = next(walk(basepath))[2]
    RMS = {}
    for result_file in result_files:
        RMS[result_file] = {}
        if result_file.startswith('SimpleBuilding') and result_file.endswith('.mat'):
            tsd_mat = TimeSeriesData(basepath.joinpath(result_file)).to_df()
            for variable in variables_building:
                plt.figure()
                fig, axs = plt.subplots(2)
                i = 0
                for zone, color in zones.items():
                    i += 1
                    variable_string = "multizone.zone[%d].%s" % (i, variable)
                    axs[0].plot(tsd_mat[variable_string], label=zone, color=color)
                axs[0].legend()
                fig.suptitle(variable)
                #error
                # Relative Percent Difference
                # error = 2 * abs((tsd_mat["multizone.zone[1].%s" % variable] - tsd_mat["multizone.zone[2].%s" % variable]) /
                #                 (tsd_mat["multizone.zone[1].%s" % variable] + tsd_mat["multizone.zone[2].%s" % variable]))
                # relative error
                error = abs(tsd_mat["multizone.zone[1].%s" % variable] - tsd_mat["multizone.zone[2].%s" % variable]) / \
                        abs(1 + tsd_mat["multizone.zone[1].%s" % variable])
                axs[1].plot(error, label="Relative Percent Difference", color="blue")
                axs[1].legend()
                # RMS
                rms = (tsd_mat["multizone.zone[1].%s" % variable] - tsd_mat["multizone.zone[2].%s" % variable]) ** 2
                if with_plot:
                    plt.show()
                RMS[result_file][variable] = math.sqrt(sum(rms)/len(rms))
    pass


if __name__ == '__main__':
    main()
