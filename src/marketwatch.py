import pandas as pd


def load_ticker_marketwatch(filename):
    df = pd.read_csv(filename)
    df.drop(df.columns[[1, 2, 3]], axis=1, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['Close'] = df['Close'].str.replace(",", "").astype(float)

    return df.iloc[::-1]
