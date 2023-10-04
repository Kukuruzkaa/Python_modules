class Account(object):
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount):
        self.value += amount
        

class Bank(object):
    """The bank"""
    
    def __init__(self):
        self.accounts = []
        
    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        if isinstance(new_account, Account):
            for i in self.accounts:
                if i.name == new_account.name:
                    print("ERROR: This account name already exists")
                    return False
                else:
                    self.accounts.append(new_account)
                    return True
        return False
        
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        # ... Your code ...
    
    def is_corrupted(account):
        accnt = dir(account)
        if len(accnt) % 2 == 0:
            return True
        for key in accnt:
            if key.startswith('b'):
                return True
        for key in accnt:
            if not key.startswith('zip') or not key.startswith('addr'):
                return True
        if not hasattr(account, 'name') or not hasattr(account, 'id') or not hasattr(account, 'value'):
            return True
        elif not isinstance(accnt.name, str):
            return True
        elif not isinstance(accnt.id, int):
            return True
        elif not isinstance(accnt.value, (int, float)):
            return True
        return False    
           
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        to_fix = None
        for i in self.accounts:
            if i.name == name:
                to_fix = self.accounts[i]
            else:
                return False
        accnt = dir(to_fix)
        for key in accnt:
            if not key.startswith('zip') or not key.startswith('addr'):
                setattr(accnt, 'zip', '000-000')
        if not hasattr(accnt, 'name'):
            setattr(accnt, 'name', 'Bob')
        elif not hasattr(accnt, 'id') or not isinstance(accnt.id, int):
            setattr(accnt, 'id', Account.ID_COUT)
            Account.ID_COUNT += 1
        elif not hasattr(accnt, 'value') or not isinstance(accnt.value, (int, float)):
            setattr(accnt, 'value', 0)
        for key in accnt:
            if key.startswith('b'):
                delattr(accnt, key)
        if len(accnt) % 2 == 0:
            setattr(accnt, 'extra field', 'optional')
        return True
        
        