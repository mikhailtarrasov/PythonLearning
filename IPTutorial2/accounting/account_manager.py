from accounting.account import Account


class AccountManager(object):
    __current_account_name = None
    __accounts = None

    def __init__(self):
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

    def __get_account(self, account_name=__current_account_name):
        if account_name is None or self.__is_account_exist(account_name):
            return None
        else:
            return (account for account in self.__accounts if account.name == account_name)

    def get_balance(self):
        if self.__current_account_name is None:
            msg = 'Error! Please select account first!'
            return msg
        
        current_account = self.__get_account()  # type: Account
        if current_account is not None:
            return current_account.balance
        else:
            msg = 'Error! Account with \'{0}\' name is not exist yet!'.format(self.__current_account_name)
            return msg

    def show_accounts(self):
        return [account.name for account in self.__accounts]
