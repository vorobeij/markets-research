from matplotlib import pyplot as plt

from src.fred import add_recession_areas


def get_cmap():
    colors = ["62EB46", "4EAEDE", "4F49F5", "D451FF", "33F5AA"]
    return list(map(lambda c: "#" + c, colors))


def draw_charts_above(mainDf, dfs, start_date):
    colors = get_cmap()
    fig, ax1 = plt.subplots(len(dfs), 1, figsize=(16, len(dfs) * 3), sharex=True)

    ax2 = ax1
    for i, df in enumerate(dfs):
        ax = ax2[i]
        ax.plot(mainDf, color="#FF5800")
        add_recession_areas(ax, start_date)

        correlation = df[df.columns.values[0]].corr(mainDf[mainDf.columns.values[0]])
        axx = ax.twinx()
        axx.set_title(df.columns.values[0] + ", corr = " + str(correlation)[0: 3])
        axx.plot(df, color=colors[i % colors.__len__()])

    fig.tight_layout()
    return fig


def draw_charts(dfs, start_date):
    colors = get_cmap()
    fig, ax1 = plt.subplots(figsize=(16, 5))

    ax = ax1
    df = dfs[0]
    j = 0
    ax.plot(df, color=colors[j % colors.__len__()])
    add_recession_areas(ax, start_date)

    for i, df in enumerate(dfs):
        axx = ax.twinx()
        axx.set_title(df.columns.values[0])
        axx.plot(df, color=colors[i % colors.__len__()])

    fig.tight_layout()
    return fig
