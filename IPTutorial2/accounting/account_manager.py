from accounting.account import Account


class AccountManager(object):

    def __init__(self):
        self.__current_account_name = None  # type: str
        self.__accounts = []  # type: Account

    def __is_account_exist(self, account_name):
        if account_name is not None:
            return account_name in (account.name for account in self.__accounts)
        else:
            return False

    def add_account(self, account_name):
        if not self.__is_account_exist(account_name):
            new_account = Account(account_name)
            self.__accounts.append(new_account)
            msg = 'Account \'{0}\' was successfully added'.format(account_name)
        else:
            msg = 'Warning! Action canceled, account with the same name already exist.'
        return msg

    def change_account(self, account_name):
        if self.__is_account_exist(account_name):
            self.__current_account_name = account_name
            msg = 'Account \'{0}\' was successfully set active!'.format(account_name)
        else:
            msg = 'Error! Account with \'{0}\' name is not exist yet!'.format(account_name)
        return msg

    def __get_account(self, account_name):
        if account_name is None or self.__is_account_exist(account_name) is False:
            return None
        else:
            return next(account for account in self.__accounts if account.name == account_name)

    def get_active_account_name(self):
        acc = self.__get_account(self.__current_account_name)
        if acc:
            return acc.name

    def get_balance(self):
        if self.__current_account_name is None:
            msg = 'Error! Please select account first!'
            return msg
        
        current_account = self.__get_account(self.__current_account_name)  # type: Account
        if current_account is not None:
            return 'The balance of your \'{0}\' account is {1}!'.format(current_account.name, current_account.balance)
        else:
            msg = 'Error! Account with \'{0}\' name is not exist yet!'.format(self.__current_account_name)
            return msg

    def show_accounts(self):
        return [account.name for account in self.__accounts]

    def add_income(self, amount):
        new_amount = float(amount) if isinstance(float(amount), float) else int(amount) if isinstance(int(amount), int) else None
        if new_amount is None:
            msg = 'Error! Please enter correct number!'
            return msg
        current_account = self.__get_account(self.__current_account_name)  # type: Account
        if current_account is not None:
            current_account.add_transaction(new_amount)
            msg = 'Income to \'{0}\' account was successfully added!'.format(current_account.name)
        else:
            msg = 'Error! Action canceled, please, select an account first!'
        return msg

    def add_expenses(self, amount):
        new_amount = float(amount) if isinstance(float(amount), float) else int(amount) if isinstance(int(amount), int) else None
        if new_amount is None:
            msg = 'Error! Please enter correct number!'
            return msg
        current_account = self.__get_account(self.__current_account_name)  # type: Account
        if current_account is not None:
            current_account.add_transaction(-new_amount)
            msg = 'Expense to \'{0}\' account was successfully added!'.format(current_account.name)
        else:
            msg = 'Error! Action canceled, please, select an account first!'
        return msg
