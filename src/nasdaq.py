from src.charts import draw_charts
from src.google_trends import load_google_trends
from src.recession import load_fred_data
from src.yahoo import load_ticker_yahoo


def nsdq():
    start_date = "2003-01-01"
    gt_files = [
        'data/gt/gt-stock-market-bubble.csv',  # look closer
        'data/gt/gt-market-bottom.csv',  # pay close attention
        'data/gt/gt-bear-market.csv',
        'data/gt/gt-bull-run.csv',
        'data/gt/gt-gas-prices.csv',
        'data/gt/gt-inflation.csv',
        'data/gt/gt-interest-rates.csv',
        'data/gt/gt-mortgage.csv',
        'data/gt/gt-refinance.csv',
        'data/gt/gt-shortage.csv',
        'data/gt/gt-treasury.csv',
        'data/gt/gt-market-crash.csv'
    ]
    charts_data = list()

    charts_data.append(load_ticker_yahoo('data/NSDQ.csv', start_date))
    charts_data.append(load_fred_data('data/fred/m2-WM2NS.csv', start_date))
    charts_data.extend(load_google_trends(gt_files, start_date))

    draw_charts(charts_data, start_date).savefig('output/nsdq.pdf')
