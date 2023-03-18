import calendar
import re

import pandas as pd


def clean_int_column(table, column_name):
    return table[column_name].replace('<1', 1)


def date_append_last_day_as_date(table, column_name):
    full_date_list = []
    for tm in table[column_name]:
        splits = tm.split('-')
        if len(splits) == 2:
            year = int(splits[0])
            month = int(splits[1])
            full_date_list.append(tm + '-' + str(calendar.monthrange(year, month)[1]))
        else:
            full_date_list.append(tm)

    return pd.to_datetime(full_date_list)


def cleanGtFile(filename):
    with open(filename, 'r') as f:
        content = f.read()
        content_new = content.replace("<1", "0")
        f.close()

    with open(filename, 'w') as f:
        f.write(content_new)
        f.close()


def set_index(table, indexColumnName):
    try:
        table[indexColumnName] = date_append_last_day_as_date(table, indexColumnName)
        table[indexColumnName] = pd.to_datetime(table[indexColumnName])

        # convert the object type columns to numeric
        for col in table.columns:
            if table[col].dtype == 'O':
                table[col] = pd.to_numeric(table[col])

        # set the index to the 'week' variable to make easy to plot with pandas
        table.set_index(indexColumnName, inplace=True)
    except:
        return


def load_gt_chart(filename, start_date):
    cleanGtFile(filename)
    table = pd.read_csv(filename, header=1)
    cols = table.columns
    # list comprehension to split name labels and use only the first name
    cols = [x.lower() for x in cols]
    table.columns = cols

    set_index(table, 'month')
    set_index(table, 'week')

    return table.query('"%s" < index' % start_date)


def load_google_trends(gt_files, start_date):
    gt_charts = list(map(lambda filename: load_gt_chart(filename, start_date), gt_files))
    return gt_charts
