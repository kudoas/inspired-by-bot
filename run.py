from slackbot.bot import Bot
from dotenv import load_dotenv

load_dotenv()


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
