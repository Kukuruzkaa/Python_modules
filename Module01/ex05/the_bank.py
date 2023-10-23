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
        if isinstance(new_account, Account):
            for i in self.accounts:
                if i.name == new_account.name:
                    print("ERROR: This account name already exists")
                    return False
            else:
                self.accounts.append(new_account)
                return True
   
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        o_account = None
        d_account = None
        if isinstance(origin, str) and isinstance(dest, str) \
            and isinstance(amount, (int, float)) and amount > 0:
            for account in self.accounts:
                if account.name == origin:
                    o_account = account
                if account.name == dest:
                    d_account = account
            if not o_account or not d_account:
                return False
            if self.is_corrupted(o_account) or self.is_corrupted(d_account):
                return False
            if  amount > o_account.value:
                # print('not enough funds to make a transfer')
                return False
            if origin != dest:
                o_account.transfer(-amount)
                d_account.transfer(amount)
            return True
            
          
    @staticmethod
    def is_corrupted(account):
        accnt = dir(account)
        if len(accnt) % 2 == 0:
            # print("Account has en even number of attributes")
            return True
        for key in accnt:
            if key.startswith('b'):
                # print("An attribute starting with b")
                return True
        if not (hasattr(account, 'zip') or not hasattr(account, 'addr')):
            # print("Missing attribute zip or addr")
            return True
        if not hasattr(account, 'name'):
            # print("Missing attribute name")
            return True
        if not hasattr(account, 'id'):
            # print("Missing attribute id")
            return True
        if not hasattr(account, 'value'):
            # print("Missing attribute value")
            return True
        if not isinstance(account.name, str):
            # print("Account name is not a string")
            return True
        if not isinstance(account.id, int):
            # print("Account id is not a number")
            return True
        if not isinstance(account.value, (int, float)):
            # print("Account value is no a number")
            return True
        return False    

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        to_fix = None
        if isinstance(name, str):
            for account in self.accounts:
                if account.name == name:
                    to_fix = account
        if isinstance(name, Account):
            to_fix = name
        if not to_fix:
            return False
        accnt = dir(to_fix)
        if not hasattr(to_fix, 'zip'):
                setattr(to_fix, 'zip', '000-000')
        elif not hasattr(to_fix, 'addr'):
                setattr(to_fix, 'addr', 'Paris, 75013')
        if not hasattr(to_fix, 'name'):
            setattr(to_fix, 'name', 'Bob')
        elif not hasattr(to_fix, 'id') or not isinstance(to_fix.id, int):
            setattr(to_fix, 'id', Account.ID_COUT)
            Account.ID_COUNT += 1
        elif not hasattr(to_fix, 'value') or not isinstance(to_fix.value, (int, float)):
            setattr(to_fix, 'value', 0)
        for key in accnt:
            if key.startswith('b'):
                b_attr = key
                delattr(to_fix, b_attr)
        accnt = dir(to_fix)
        if len(accnt) % 2 == 0:
            if not hasattr(to_fix, 'extra'):
                setattr(to_fix, 'extra', 'optional')
            elif not hasattr(to_fix, 'extra2', 'optional too'):
                setattr(to_fix, 'extra2', 'optional too')
            else:
                delattr(to_fix, 'extra2')
        return True
        
# if __name__ == "__main__":
    
#     bank = Bank()
#     #1
#     john = Account(
#     'William John',
#     zip='100-064',
#     brother="heyhey",
#     value=6460.0,
#     ref='58ba2b9954cd278eda8a84147ca73c87',
#     info=None,
#     other='This is the vice president of the corporation',
#     lol = "hihi"
#     )
    
#     print("Account corrupted:", bank.is_corrupted(john))
#     bank.add(john)
#     # print(bank.fix_account(john))

#     print("Account fixed:", bank.fix_account('William John'))
    
#     #2
#     john = Account(
#     'William John',
#     zip='100-064',
#     rother="heyhey",
#     value=6460.0,
#     ref='58ba2b9954cd278eda8a84147ca73c87',
#     info=None,
#     other='This is the vice president of the corporation',
#     )

#     print("Account corrupted:", bank.is_corrupted(john))
    
#     #3
#     john = Account(
#     'William John',
#     zip='100-064',
#     rother="heyhey",
#     ref='58ba2b9954cd278eda8a84147ca73c87',
#     info=None,
#     other='This is the vice president of the corporation',
#     lol = "lolilol"
#     )
#     print("Account corrupted:", bank.is_corrupted(john))
#     print(john.__dict__)
    
#     #4
#     bank.add(
#     Account(
#         'Jane',
#         zip='911-745',
#         value=1000.0,
#         ref='1044618427ff2782f0bbece0abd05f31')
#     )   

#     jhon = Account(
#         'Jhon',
#         zip='911-745',
#         value=1000.0,
#         ref='1044618427ff2782f0bbece0abd05f31'
#     )

#     bank.add(jhon)

#     print("testing a valid transfer")
#     print(jhon.value)
#     print(bank.transfer("Jane", "Jhon", 500))
#     print(jhon.value)
    
#     #5
#     print(bank.transfer("Jane", "Jhon", 1000))
#     print(jhon.value)