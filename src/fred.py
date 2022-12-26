import os
import urllib.request

import pandas as pd


def add_recession_areas(ax, start_date):
    column_name = 'Recessions'
    df = reload_fred_data('JHDUSRGDPBR', 'Recessions', startdate=start_date, reload=False)  # Recessions are not so often to reload them each time
    df['match'] = df[column_name].eq(df[column_name].shift())
    df = df.loc[df['match'] == False]
    df.drop(columns=['match'], inplace=True)
    index_prev = None
    for index, row in df.iterrows():
        if row[column_name] == 0.0 and index_prev is not None:
            ax.axvspan(index_prev, index, alpha=0.05, color='black')
        index_prev = index


def reload_fred_data(symbol, label, startdate, reload=True):
    url = fred_url(symbol)
    filename = 'data/fred/' + symbol + '.csv'
    if reload:
        print("loading " + url)
        os.remove(filename)
        urllib.request.urlretrieve(url, filename)

    df = pd.read_csv(filename)
    df['DATE'] = pd.to_datetime(df['DATE'])
    df.set_index('DATE', inplace=True)

    df = df.drop(df[df[df.columns.values[0]].map(lambda x: str(x) == ".")].index)
    df[label] = df[df.columns.values[0]]
    df = df.drop(columns=[df.columns.values[0]])

    df[label] = df[label].astype(float)

    return df.query('"%s" < index' % startdate)


def fred_url(symbol):
    return 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=' + symbol + '&cosd=1900-01-01&coed=2022-11-01&fq=Monthly'
