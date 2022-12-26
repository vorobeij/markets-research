from src.charts import draw_charts
from src.fred import reload_fred_data
from src.google_trends import load_google_trends
from src.yahoo import load_ticker_yahoo


def spx():
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
    reload = True
    charts_data.append(load_ticker_yahoo('^GSPC', start_date, reload=reload))
    charts_data.append(reload_fred_data('WM2NS', "M2 (WM2NS)", start_date, reload=reload))
    charts_data.append(reload_fred_data('RESPPLLOPNWW', "Liabilities and Capital: Liabilities: Earnings Remittances Due to the U.S. Treasury: Wednesday Level (RESPPLLOPNWW)", start_date, reload=reload))
    charts_data.append(reload_fred_data('WALCL', "Assets: Total Assets: Total Assets (Less Eliminations from Consolidation): Wednesday Level (WALCL)", start_date, reload=reload))
    charts_data.append(reload_fred_data('GFDEGDQ188S', "Federal Debt: Total Public Debt as Percent of Gross Domestic Product (GFDEGDQ188S)", start_date, reload=reload))
    charts_data.append(reload_fred_data('FPCPITOTLZGUSA', "Inflation, consumer prices for the United States (FPCPITOTLZGUSA)", start_date, reload=reload))
    charts_data.append(reload_fred_data('PPIACO', "Producer Price Index by Commodity: All Commodities (PPIACO)", start_date, reload=reload))
    charts_data.append(reload_fred_data('NFCI', "Chicago Fed National Financial Conditions Index (NFCI)", start_date, reload=reload))
    charts_data.append(reload_fred_data('DPRIME', "Bank Prime Loan Rate (DPRIME)", start_date, reload=reload))
    charts_data.append(reload_fred_data('IIPUSNETIQ', "U.S. Net International Investment Position (IIPUSNETIQ)", start_date, reload=reload))
    charts_data.append(reload_fred_data('UMCSENT', "University of Michigan: Consumer Sentiment (UMCSENT)", start_date, reload=reload))
    charts_data.append(reload_fred_data('JTSJOL', "Job Openings: Total Nonfarm (JTSJOL)", start_date, reload=reload))
    charts_data.append(reload_fred_data('RRPONTSYD', "Overnight Reverse Repurchase Agreements: Treasury Securities Sold by the Federal Reserve in the Temporary Open Market Operations (RRPONTSYD)", start_date, reload=reload))
    charts_data.append(reload_fred_data('TOTALSA', "Total Vehicle Sales (TOTALSA)", start_date, reload=reload))
    charts_data.append(reload_fred_data('AISRSA', "Auto Inventory/Sales Ratio (AISRSA)", start_date, reload=reload))
    charts_data.append(reload_fred_data('COMREPUSQ159N', "Commercial Real Estate Prices for United States (COMREPUSQ159N)", start_date, reload=reload))
    charts_data.append(reload_fred_data('BCNSDODNS', "Nonfinancial Corporate Business; Debt Securities and Loans; Liability, Level (BCNSDODNS)", start_date, reload=reload))
    charts_data.append(reload_fred_data('CPIAUCSL', "Consumer Price Index for All Urban Consumers: All Items in U.S. City Average (CPIAUCSL)", start_date, reload=reload))
    charts_data.append(reload_fred_data('CIVPART', "Labor Force Participation Rate (CIVPART)", start_date, reload=reload))
    charts_data.append(reload_fred_data('M2V', "Velocity of M2 Money Stock (M2V)", start_date, reload=reload))
    charts_data.append(reload_fred_data('PSAVERT', "Personal Saving Rate (PSAVERT)", start_date, reload=reload))
    charts_data.append(reload_fred_data('TDSP', "Household Debt Service Payments as a Percent of Disposable Personal Income (TDSP)", start_date, reload=reload))

    draw_charts(charts_data, start_date).savefig('output/nsdq-fred.pdf')

    charts_data.clear()
    charts_data.append(load_ticker_yahoo('^GSPC', start_date, reload=reload))
    charts_data.extend(load_google_trends(gt_files, start_date))
    draw_charts(charts_data, start_date).savefig('output/nsdq-google-trends.pdf')
