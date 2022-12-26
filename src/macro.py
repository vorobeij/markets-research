from src.charts import draw_charts
from src.fred import load_fred_data
from src.google_trends import load_google_trends
from src.yahoo import load_ticker_yahoo


def macro():
    start_date = "2003-01-01"

    charts_data = list()

    charts_data.append(load_ticker_yahoo('data/NSDQ.csv', start_date))
    charts_data.append(load_fred_data('data/fred/WM2NS.csv', "M2 (WM2NS)", start_date))
    charts_data.append(load_fred_data('data/fred/RESPPLLOPNWW.csv', "Liabilities and Capital: Liabilities: Earnings Remittances Due to the U.S. Treasury: Wednesday Level (RESPPLLOPNWW)", start_date))
    charts_data.append(load_fred_data('data/fred/WALCL.csv', "Assets: Total Assets: Total Assets (Less Eliminations from Consolidation): Wednesday Level (WALCL)", start_date))
    charts_data.append(load_fred_data('data/fred/GFDEGDQ188S.csv', "Federal Debt: Total Public Debt as Percent of Gross Domestic Product (GFDEGDQ188S)", start_date))
    charts_data.append(load_fred_data('data/fred/FPCPITOTLZGUSA.csv', "Inflation, consumer prices for the United States (FPCPITOTLZGUSA)", start_date))
    charts_data.append(load_fred_data('data/fred/PPIACO.csv', "Producer Price Index by Commodity: All Commodities (PPIACO)", start_date))
    charts_data.append(load_fred_data('data/fred/NFCI.csv', "Chicago Fed National Financial Conditions Index (NFCI)", start_date))
    charts_data.append(load_fred_data('data/fred/DPRIME.csv', "Bank Prime Loan Rate (DPRIME)", start_date))
    charts_data.append(load_fred_data('data/fred/IIPUSNETIQ.csv', "U.S. Net International Investment Position (IIPUSNETIQ)", start_date))
    charts_data.append(load_fred_data('data/fred/UMCSENT.csv', "University of Michigan: Consumer Sentiment (UMCSENT)", start_date))
    charts_data.append(load_fred_data('data/fred/JTSJOL.csv', "Job Openings: Total Nonfarm (JTSJOL)", start_date))
    charts_data.append(load_fred_data('data/fred/RRPONTSYD.csv', "Overnight Reverse Repurchase Agreements: Treasury Securities Sold by the Federal Reserve in the Temporary Open Market Operations (RRPONTSYD)", start_date))
    charts_data.append(load_fred_data('data/fred/TOTALSA.csv', "Total Vehicle Sales (TOTALSA)", start_date))
    charts_data.append(load_fred_data('data/fred/AISRSA.csv', "Auto Inventory/Sales Ratio (AISRSA)", start_date))
    charts_data.append(load_fred_data('data/fred/COMREPUSQ159N.csv', "Commercial Real Estate Prices for United States (COMREPUSQ159N)", start_date))
    charts_data.append(load_fred_data('data/fred/BCNSDODNS.csv', "Nonfinancial Corporate Business; Debt Securities and Loans; Liability, Level (BCNSDODNS)", start_date))
    charts_data.append(load_fred_data('data/fred/CPIAUCSL.csv', "Consumer Price Index for All Urban Consumers: All Items in U.S. City Average (CPIAUCSL)", start_date))
    # todo merge
    charts_data.append(load_fred_data('data/fred/CIVPART.csv', "Labor Force Participation Rate (CIVPART)", start_date))
    charts_data.append(load_fred_data('data/fred/M2V.csv', "Velocity of M2 Money Stock (M2V)", start_date))
    # todo these two on one chart!
    charts_data.append(load_fred_data('data/fred/PSAVERT.csv', "Personal Saving Rate (PSAVERT)", start_date))
    charts_data.append(load_fred_data('data/fred/TDSP.csv', "Household Debt Service Payments as a Percent of Disposable Personal Income (TDSP)", start_date))

    draw_charts(charts_data, start_date).savefig('output/nsdq-fred.pdf')

    charts_data.clear()
    charts_data.append(load_ticker_yahoo('data/NSDQ.csv', start_date))
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
    charts_data.extend(load_google_trends(gt_files, start_date))
    draw_charts(charts_data, start_date).savefig('output/nsdq-google-trends.pdf')
