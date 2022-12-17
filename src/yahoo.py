import pandas as pd


def load_ticker_yahoo(filename, startdate):
    df = pd.read_csv(filename)
    df.drop(df.columns[[1, 2, 3, 4, 6]], axis=1, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df.query('"%s" < index' % startdate)
