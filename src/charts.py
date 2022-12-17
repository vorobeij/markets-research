import numpy
from matplotlib import pyplot as plt

from src.recession import add_recession_areas


def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)


def draw_charts(dfs, start_date):
    fig, ax1 = plt.subplots(len(dfs), 1, figsize=(16, len(dfs) * 3), sharex=True)

    ax = ax1
    for i, df in enumerate(dfs):
        ax[i].set_title(df.columns.values[0])
        ax[i].plot(df, color=numpy.random.rand(3, ))
        add_recession_areas(ax[i], start_date)

    fig.tight_layout()
    return fig
