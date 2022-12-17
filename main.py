from src.google_trends import load_gt
from src.recession import add_recession_areas
from src.yahoo import load_ticker_yahoo

if __name__ == '__main__':
    start_date = "2003-01-01"

    gt_files = [
        # 'data/gt/gt-inflation.csv',
        # 'data/gt/gt-interest-rates.csv',
        'data/gt/gt-bull-run.csv'
    ]
    gtrends_charts_df = load_gt(gt_files)

    nsdq = load_ticker_yahoo('data/NSDQ.csv', start_date)

    plot = nsdq.plot()
    add_recession_areas(plot, start_date)

    fig = gtrends_charts_df.plot(secondary_y=True, logy=True, ax=plot, figsize=(16, 9)).get_figure()
    fig.tight_layout()
    fig.savefig('output/plot.jpg')
