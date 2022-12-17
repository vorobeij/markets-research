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
    gt_charts_df = load_gt(gt_files)

    gt_charts_df.plot(figsize=(14, 6))

    nsdq = load_ticker_yahoo('data/NSDQ.csv', start_date)
    print(nsdq.head())

    ax = nsdq.plot()
    add_recession_areas(ax, start_date)
    gt_charts_fig = gt_charts_df.plot(secondary_y=True, logy=True, ax=ax, figsize=(14, 6)).get_figure()
    gt_charts_fig.savefig('output/plot.jpg')
