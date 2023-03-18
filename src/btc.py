from src.charts import draw_charts_above
from src.google_trends import load_google_trends
from src.yahoo import load_ticker_yahoo


def btc():
    start_date = "2015-01-01"
    gt_files = [
        'data/gt/gt-crypto-5y.csv',
        'data/gt/gt-bitcoin-price-5y.csv',
        'data/gt/gt-bitcoin-5y.csv'
    ]
    charts_data = list()
    charts_data.extend(load_google_trends(gt_files, start_date))
    btc_df = load_ticker_yahoo('BTC-USD', start_date)

    draw_charts_above(btc_df, charts_data, start_date).savefig('output/btc.pdf')
