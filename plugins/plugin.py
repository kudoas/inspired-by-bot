import re

from slackbot.bot import Bot, respond_to

from .scraping import get_title, get_qiita_trand_title


@respond_to('他は？')
def simple_reply(message):
    print(message.body)
    message.reply('モスもいいよ！')


@respond_to(r'^url\s+\S.*')
def return_content_title(message):
    text = message.body['text']
    s, url = text.split(None, 1)
    url = url[1:-1]
    title = get_title(url)
    message.reply(title)


@respond_to('trand')
def return_trand_qiita(message):
    trand = get_qiita_trand_title()
    message.reply(trand[0])
