import pandas as pd
import yfinance as yf


def load_ticker_yahoo(ticker, startdate, reload=True):
    filename = 'data/' + ticker + ".csv"
    if reload:
        df = yf.download(ticker, start=startdate)
        df.to_csv(filename)
    df = pd.read_csv(filename)
    df.drop(df.columns[[1, 2, 3, 4, 6]], axis=1, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df.query('"%s" < index' % startdate)
