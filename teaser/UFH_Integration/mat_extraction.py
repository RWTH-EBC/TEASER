import math
import pathlib
import numpy as np
import matplotlib.pyplot as plt
from ebcpy import TimeSeriesData
from os import walk


def main(with_plot=True):
    variables_building = ['ROM.intGainsConv.T', 'ROM.intGainsConv.Q_flow', 'ROM.intGainsRad.T', 'ROM.intGainsRad.Q_flow']
    variables_discr = ['vol2.T', 'vol2.heatPort.Q_flow', 'vol1.T', 'vol2.heatPort.Q_flow']
    zones = {'as Walls': 'blue', 'as Tabs': 'red'}
    basepath = pathlib.Path(__file__).parents[4].joinpath("Dymola_results")
    result_files = next(walk(basepath))[2]
    RMS = {}
    for result_file in result_files:
        RMS[result_file] = {}
        if result_file.startswith('SimpleBuilding') and result_file.endswith('.mat'):
            continue
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
                fig.suptitle(result_file.replace('SimpleBuildingext_', '') + variable)
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
        if result_file.startswith('Discretisation') and result_file.endswith('.mat'):
            tsd_mat = TimeSeriesData(basepath.joinpath(result_file)).to_df()
            plt.figure()
            fig, axs = plt.subplots(2)
            axs[0].plot(tsd_mat[variables_discr[0]], label=1, color='blue')
            axs[0].plot(tsd_mat[variables_discr[2]], label=2, color='red')
            axs[0].legend()
            fig.suptitle(result_file + 'vol temperature')
            # error
            # Relative Percent Difference
            # error = 2 * abs((tsd_mat["multizone.zone[1].%s" % variable] - tsd_mat["multizone.zone[2].%s" % variable]) /
            #                 (tsd_mat["multizone.zone[1].%s" % variable] + tsd_mat["multizone.zone[2].%s" % variable]))
            # relative error
            error = abs(tsd_mat[variables_discr[0]] - tsd_mat[variables_discr[2]]) / \
                    abs(1 + tsd_mat[variables_discr[0]])
            axs[1].plot(error, label="Relative Percent Difference", color="blue")
            axs[1].legend()
            # RMS
            # rms = (tsd_mat["multizone.zone[1].%s" % variable] - tsd_mat["multizone.zone[2].%s" % variable]) ** 2
            if with_plot:
                plt.show()
            # RMS[result_file][variable] = math.sqrt(sum(rms) / len(rms))
            plt.figure()
            fig, axs = plt.subplots(2)
            axs[0].plot(tsd_mat[variables_discr[1]], label=1, color='blue')
            axs[0].plot(tsd_mat[variables_discr[3]], label=2, color='red')
            axs[0].legend()
            fig.suptitle(result_file + 'vol temperature')

            error = abs(tsd_mat[variables_discr[1]] - tsd_mat[variables_discr[3]]) / \
                    abs(1 + tsd_mat[variables_discr[1]])
            axs[1].plot(error, label="Relative Percent Difference", color="blue")
            axs[1].legend()
            if with_plot:
                plt.show()

    pass


if __name__ == '__main__':
    main()
