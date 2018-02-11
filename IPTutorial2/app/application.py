from accounting.account_manager import AccountManager
from telegram.ext import Updater, CommandHandler
from app import config


class App(object):
    bot_updater = None  # type: Updater
    account_manager = None  # type: AccountManager

    example_account_name = 'AccountName'
    example_add_account_command = '/add_account {0}'.format(example_account_name)
    example_change_account_command = '/change_account {0}'.format(example_account_name)
    example_get_balance = '/get_balance'
    example_amount_value = '123.45'
    example_add_income_command = '/add_income {0}'.format(example_amount_value)
    example_add_expense_command = '/add_expense {0}'.format(example_amount_value)

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
        dp.add_handler(CommandHandler("get_balance", self.command_get_balance))
        dp.add_handler(CommandHandler("add_income", self.command_add_income, pass_args=True))
        dp.add_handler(CommandHandler("add_expense", self.command_add_expense, pass_args=True))

    def command_start(self, bot, update):
        update.message.reply_text('Welcome, {0}!\n'.format(update.effective_user.first_name))
        self.command_help(bot, update)

    def get_active_account_name(self):
        return self.account_manager.get_active_account_name()

    def active_account(self):
        name = self.get_active_account_name()
        if name is not None:
            msg = "Active account is '{0}'".format(name)
        else:
            msg = "No account selected"
        return msg

    def command_help(self, bot, update):
        update.message.reply_text('{0}\n\n'.format(self.active_account())
                                  + 'Available commands:\n'
                                  + '/show_accounts\n'
                                  + '{0}\n'.format(self.example_add_account_command)
                                  + '{0}\n'.format(self.example_change_account_command)
                                  + '{0}\n'.format(self.example_get_balance)
                                  + '{0}\n'.format(self.example_add_income_command)
                                  + '{0}\n'.format(self.example_add_expense_command)
                                  + '/help')

    def command_show_accounts(self, bot, update):
        accounts = self.account_manager.show_accounts()
        msg = 'There are no created accounts'
        if accounts:
            msg = "Accounts:\n-\t" + \
                  "\n-\t".join(accounts)
        update.message.reply_text(msg)

    def command_add_account(self, bot, update, args):
        account_name = None if args is None or not args else args[0]
        if account_name is None:
            msg = 'Please, enter account name after command.\n' \
                  'Example: {0}'.format(self.example_add_account_command)
        if account_name is not None:
            msg = self.account_manager.add_account(account_name)
        update.message.reply_text(msg)

    def command_change_account(self, bot, update, args):
        account_name = None if args is None or not args else args[0]
        if account_name is None:
            msg = 'Please, enter account name after command.\n' \
                  'Example: {0}'.format(self.example_change_account_command)
        else:
            msg = self.account_manager.change_account(account_name)
        update.message.reply_text(msg)

    def command_get_balance(self, bot, update):
        update.message.reply_text(self.account_manager.get_balance())

    def command_add_income(self, bot, update, args):
        amount = None if args is None or not args else args[0]
        if amount is None:
            msg = 'Please, enter income amount after command.\n' \
                  'Example: {0}'.format(self.example_add_income_command)
        else:
            msg = self.account_manager.add_income(amount)
        update.message.reply_text(msg)

    def command_add_expense(self, bot, update, args):
        amount = None if args is None or not args else args[0]
        if amount is None:
            msg = 'Please, enter expense amount after command.\n' \
                  'Example: {0}'.format(self.example_add_expense_command)
        else:
            msg = self.account_manager.add_expenses(amount)
        update.message.reply_text(msg)
