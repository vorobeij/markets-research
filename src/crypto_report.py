from matplotlib import pyplot as plt

from src.btc import btc
from src.fred import add_recession_areas


def get_cmap():
    colors = ["99d98c", "76c893", "52b69a", "34a0a4", "168aad", "1a759f", "1e6091", "184e77"]
    return list(map(lambda c: "#" + c, colors))


def draw_charts(dfs, start_date):
    colors = get_cmap()
    fig, ax1 = plt.subplots(len(dfs), 1, figsize=(16, len(dfs) * 3), sharex=True)

    ax = ax1
    for i, df in enumerate(dfs):
        ax[i].set_title(df.columns.values[0])
        ax[i].plot(df, color=colors[i % colors.__len__()])
        add_recession_areas(ax[i], start_date)

    fig.tight_layout()
    return fig


def crypto_report():
    btc()
