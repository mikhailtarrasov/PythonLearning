import logging

from app import config, logger
import telegram
from telegram.ext import Updater, CommandHandler


class App(object):
    bot_updater = None #type: Updater

    def __init__(self, params: dict = None):
        self.bot_updater = Updater(config.token)

        self.configurate()

        self.bot_updater.start_polling()
        self.bot_updater.idle()

    def configurate(self):
        dp = self.bot_updater.dispatcher
        dp.add_handler(CommandHandler("start", self.command_start))

    def command_start(self, bot, update):
        update.message.reply_text('Start!')
