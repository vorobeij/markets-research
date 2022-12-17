import calendar

import pandas as pd


def clean_int_column(table, column_name):
    return table[column_name].replace('<1', 1)


def date_append_last_day_as_date(table, column_name):
    full_date_list = []
    for tm in table[column_name]:
        year = int(tm.split('-')[0])
        month = int(tm.split('-')[1])
        full_date_list.append(tm + '-' + str(calendar.monthrange(year, month)[1]))

    return pd.to_datetime(full_date_list)


def load_gt_chart(filename):
    table = pd.read_csv(filename, header=1)
    cols = table.columns
    # list comprehension to split name labels and use only the first name
    cols = [x.split()[0].lower() if len(x.split()) > 2 else x.lower() for x in cols]
    table.columns = cols

    table['month'] = date_append_last_day_as_date(table, 'month')
    table['month'] = pd.to_datetime(table['month'])

    # candidates['inflation: (worldwide)'] = clean_int_column(candidates, 'inflation: (worldwide)') todo

    # convert the object type columns to numeric
    for col in table.columns:
        if table[col].dtype == 'O':
            table[col] = pd.to_numeric(table[col])

    # set the index to the 'week' variable to make easy to plot with pandas
    table.set_index('month', inplace=True)

    return table


def load_gt(gt_files):
    gt_charts = list(map(lambda filename: load_gt_chart(filename), gt_files))

    gt_charts_df = gt_charts[0]

    for gt in gt_charts:
        gt_charts_df[gt.columns.values[0]] = gt[gt.columns.values[0]]

    return gt_charts_df
