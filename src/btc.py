from src.charts import draw_charts
from src.google_trends import load_google_trends
from src.yahoo import load_ticker_yahoo


def btc():
    start_date = "2015-01-01"
    gt_files = [
        'data/gt/gt-crypto-winter.csv',
        'data/gt/gt-meme-coin.csv',
        'data/gt/gt-stock-market-bubble.csv'
    ]

    charts_data = list()
    charts_data.append(load_ticker_yahoo('data/BTC-USD.csv', start_date))
    charts_data.extend(load_google_trends(gt_files, start_date))

    draw_charts(charts_data, start_date).savefig('output/btc.pdf')
