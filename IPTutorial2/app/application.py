# from . logger import Logger
# import telegram
from telegram.ext import Updater, CommandHandler
from IPTutorial2 import config


class App(object):
    bot_updater = None  # type: Updater

    def __init__(self, params: dict = None):
        self.bot_updater = Updater(config.BOT_TOKEN)

        self.configurate()

        self.bot_updater.start_polling()
        self.bot_updater.idle()

    def configurate(self):
        dp = self.bot_updater.dispatcher
        dp.add_handler(CommandHandler("start", self.command_start))

    def command_start(self, bot, update):
        update.message.reply_text('Start!')
