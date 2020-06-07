from slackbot.bot import Bot, respond_to


@respond_to('他は？')
def love(message):
    print(message.body)
    message.reply('モスもいいよ！')
