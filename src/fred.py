import pandas as pd


def load_fred_data(filename, label, startdate):
    df = pd.read_csv(filename)
    df['DATE'] = pd.to_datetime(df['DATE'])
    df.set_index('DATE', inplace=True)

    df = df.drop(df[df[df.columns.values[0]].map(lambda x: str(x) == ".")].index)
    df[label] = df[df.columns.values[0]]
    df = df.drop(columns=[df.columns.values[0]])

    df[label] = df[label].astype(float)

    return df.query('"%s" < index' % startdate)


def add_recession_areas(ax, start_date):
    column_name = 'Recessions'
    df = load_fred_data('data/fred/JHDUSRGDPBR.csv', 'Recessions', startdate=start_date)
    df['match'] = df[column_name].eq(df[column_name].shift())
    df = df.loc[df['match'] == False]
    df.drop(columns=['match'], inplace=True)
    index_prev = None
    for index, row in df.iterrows():
        if row[column_name] == 0.0 and index_prev is not None:
            ax.axvspan(index_prev, index, alpha=0.05, color='black')
        index_prev = index