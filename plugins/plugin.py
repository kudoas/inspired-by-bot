import re

from slackbot.bot import Bot, respond_to

from .scrap import get_title, get_qiita_trend
from .utils import get_datetime


@respond_to('説明')
def simple_reply(message):
    print(message.body)
    message.reply('Qiitaのトレンド記事を押してくれるbotです！')


@respond_to(r'^url\s+\S.*')
def return_content_title(message):
    text = message.body['text']
    s, url = text.split(None, 1)
    url = url[1:-1]
    title = get_title(url)
    message.reply(title)


@respond_to(r'^trend\s+\S.*')
def return_trend_qiita(message):
    text = message.body['text']
    s, num = text.split(None, 1)
    trend = get_qiita_trend(int(num))
    return_message = get_datetime() + '現在のQiitaのトレンド記事です' + '\n\n'
    for i in range(len(trend)):
        return_message += trend[i][0] + '\n' + trend[i][1] + '\n'
    message.reply(return_message)
