import datetime


def get_datetime():
    dt_now = datetime.datetime.now()
    date = dt_now.strftime('%Y年%m月%d日%H:%M')
    return date

