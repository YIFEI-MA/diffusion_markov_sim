import future.utils
import matplotlib
import matplotlib.pyplot as plt
from ndlib.viz.mpl.DiffusionViz import DiffusionPlot


def __plot__(self, filename=None, percentile=90, statuses=None):
    """
    Generates the plot

    :param filename: Output filename
    :param percentile: The percentile for the trend variance area
    :param statuses: List of statuses to plot. If not specified all statuses trends will be shown.
    """

    pres = self.iteration_series(percentile)
    # infos = self.model.get_info()
    # descr = ""

    plt.figure(figsize=(20, 10))

    # for k, v in future.utils.iteritems(infos):
    #     descr += "%s: %s, " % (k, v)
    # descr = descr[:-2].replace("_", " ")

    mx = 0
    i = 0
    for k, l in future.utils.iteritems(pres):

        if statuses is not None and self.srev[k] not in statuses:
            continue
        mx = len(l[0])
        if self.normalized:
            plt.plot(list(range(0, mx)), l[1] / self.nnodes, lw=2, label=self.srev[k], alpha=0.5)  # , color=cols[i])
            plt.fill_between(list(range(0, mx)), l[0] / self.nnodes, l[2] / self.nnodes, alpha=0.2)
            # ,color=cols[i])
        else:
            plt.plot(list(range(0, mx)), l[1], lw=2, label=self.srev[k], alpha=0.5)  # , color=cols[i])
            plt.fill_between(list(range(0, mx)), l[0], l[2], alpha=0.2)  # ,color=cols[i])

        i += 1

    plt.grid(axis="y")
    # plt.title(descr)
    plt.xlabel("Iterations", fontsize=24)
    plt.ylabel(self.ylabel, fontsize=24)
    plt.legend(loc="best", fontsize=18)
    plt.xlim((0, mx))

    plt.tight_layout()
    if filename is not None:
        plt.savefig(filename)
        plt.show()
        plt.clf()
    else:
        plt.show()


def setup_viz():
    # matplotlib.use('TkAgg')
    DiffusionPlot.plot = __plot__
    # reset to default backend
    matplotlib.pyplot.switch_backend(matplotlib.rcsetup._auto_backend_sentinel)
    print("Backend is now reset to: ", matplotlib.get_backend())
