from src.charts import draw_charts
from src.data import gt_files
from src.google_trends import load_google_trends


def google_trends_report():
    start_date = "2003-01-01"
    gt_filess = gt_files()

    charts_data = list()
    charts_data.extend(load_google_trends(gt_filess, start_date))
    draw_charts(charts_data, start_date).savefig('output/spx-google-trends.pdf')
