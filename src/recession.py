import pandas as pd


def load_fred_data(filename, startdate):
    df = pd.read_csv(filename)
    df['DATE'] = pd.to_datetime(df['DATE'])
    df.set_index('DATE', inplace=True)
    return df.query('"%s" < index' % startdate)


def add_recession_areas(ax, start_date):
    column_name = 'JHDUSRGDPBR'
    df = load_fred_data('data/fred/recessions-JHDUSRGDPBR.csv', startdate=start_date)
    df['match'] = df[column_name].eq(df[column_name].shift())
    df = df.loc[df['match'] == False]
    df.drop(columns=['match'], inplace=True)
    index_prev = None
    for index, row in df.iterrows():
        if row[column_name] == 0.0 and index_prev is not None:
            ax.axvspan(index_prev, index, alpha=0.05, color='black')
        index_prev = index
