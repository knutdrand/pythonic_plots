"""Main module."""
from dataclasses import dataclass
from itertools import groupby
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


@dataclass
class LazyPlot:
    func_names: list
    args_list: list
    kwargs_list: list

    def __add__(self, other):
        return self.__class__(self.func_names+other.func_names,
                              self.args_list + other.args_list,
                              self.kwargs_list + other.kwargs_list)

    def __iter__(self):
        return zip(self.func_names, self.args_list, self.kwargs_list)

    def __call__(self, ax):
        for name, args, kwargs in self:
            getattr(ax, name)(*args, **kwargs)


"""
TODO: getattr should return a callable that returns a lazyplot
"""


class Module:

    def show(self, lazy_plot_struct, n_row=None, n_col=None, show=True, sharex=False, sharey=False):
        if len(lazy_plot_struct) == 0:
            return
        if isinstance(lazy_plot_struct[0], LazyPlot):
            n_plots = len(lazy_plot_struct)
            if n_row is None and n_col is None:
                n_row, n_col = (n_plots, 1)
            elif n_row is None:
                n_row = (n_plots-1) // n_col + 1
            elif n_col is None:
                n_col = (n_plots-1) // n_row + 1
            assert n_col*n_row >= n_plots
            lazy_plot_struct = [[pair[1] for pair in group]
                                for _, group in groupby(enumerate(lazy_plot_struct), lambda pair: pair[0]//n_col)]
        else:
            max_row = max(len(row) for row in lazy_plot_struct)
            n_row, n_col = (len(lazy_plot_struct), max_row)

        fig, axes = plt.subplots(n_row, n_col, sharex=sharex, sharey=sharey)
        axes = axes.reshape(n_row, n_col)  # plt squeezes array
        for row, ax_row in zip(lazy_plot_struct, axes):
            for lazy_plot, ax in zip(row, ax_row):
                lazy_plot(ax)
                ax.label_outer()
        if show:
            plt.show()
        return fig, axes

    def save(self, lazy_plot_struct, filename):
        self.show(lazy_plot_struct, show=False)
        plt.savefig(filename)

    def show2(self, lazy_plot_struct):
        fig = plt.figure()
        g = gridspec.GridSpec(len(lazy_plot_struct), 1, figure=fig)
        for row, row_spec in zip(lazy_plot_struct, g):
            n_col = len(row)
            col_grid = gridspec.GridSpecFromSubplotSpec(1, n_col, subplot_spec=row_spec)
            for lazy_plot, cell_spec in zip(row, col_grid):
                if lazy_plot is not None:
                    ax = fig.add_subplot(cell_spec)
                    lazy_plot(ax)
        plt.show()

    def __dir__(self):
        return ["plot"] + [name for name in dir(plt) if callable(getattr(plt.Axes, name))]

    def __getattr__(self, name):
        def lazy_func(*args, **kwargs):
            return LazyPlot([name], [args], [kwargs])
        lazy_func.__name__ = f"lazy_{name}"
        lazy_func.__qualname__ = f"lazy_{name}"
        return lazy_func

