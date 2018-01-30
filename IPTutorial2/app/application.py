# from . logger import Logger
# import telegram
from accounting.account_manager import AccountManager
from telegram.ext import Updater, CommandHandler
from app import config


class App(object):
    bot_updater = None  # type: Updater
    account_manager = None  # type: AccountManager

    add_account_command_example = '/add_account {ACCOUNT NAME}'

    def __init__(self, params: dict = None):
        self.bot_updater = Updater(config.token)
        self.account_manager = AccountManager()

        self.configurate()

        self.bot_updater.start_polling()
        self.bot_updater.idle()

    def configurate(self):
        dp = self.bot_updater.dispatcher
        dp.add_handler(CommandHandler("start", self.command_start))
        dp.add_handler(CommandHandler("help", self.command_help))
        dp.add_handler(CommandHandler("show_accounts", self.command_show_accounts))
        dp.add_handler(CommandHandler("add_account", self.command_add_account, pass_args=True))
        dp.add_handler(CommandHandler("change_account", self.command_change_account, pass_args=True))

    def command_start(self, bot, update):
        update.message.reply_text('Welcome!\nAvailable commands:')
        self.command_help(bot, update)

    def command_help(self, bot, update):
        update.message.reply_text('/show_accounts\n'
                                  + '{0}\n'.format(self.add_account_command_example)
                                  + '/change_account {ACCOUNT NAME}\n'
                                  + '/get_balance')

    def command_show_accounts(self, bot, update):
        accounts = self.account_manager.show_accounts()
        msg = 'There are no created accounts' if accounts.__len__() == 0 else accounts
        update.message.reply_text(msg)

    def command_add_account(self, bot, update, account_name):
        msg = self.account_manager.add_account(account_name)
        if msg is None:
            msg = 'Please, enter account name after command.\n' \
                  'Example: {0}'.format(self.add_account_command_example)
        update.message.reply_text(msg)

    def command_change_account(self, bot, update, account_name):
        msg = self.account_manager.change_account(account_name)
        update.message.reply_text(msg)
