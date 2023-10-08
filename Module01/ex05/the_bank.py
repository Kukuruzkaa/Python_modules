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
   
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        o_account = None
        d_account = None
        for account in self.accounts:
            if account.name == dest:
                d_account = account
            elif account.name == origin:
                o_account = dest
        if not d_account:
            print('no')
        if not o_account or not d_account \
            or not isinstance(amount, (int, float)) \
            or amount > o_account.value:
                print('la')
                return False
        # if self.is_corrupted(origin) or self.is_corrupted(dest):
        #     print('la')
        #     return False
        print(o_account.value)
        print(d_account.value)
        
        if origin != dest:
            o_account.transfer(-amount)
            d_account.transfer(amount)
        return True
            
   
        
    @staticmethod
    def is_corrupted(account):
        accnt = dir(account)
        if len(accnt) % 2 == 0:
            print("Account has en even number of attributes")
            return True
        for key in accnt:
            if key.startswith('b'):
                print("An attribute starting with b")
                return True
        if not hasattr(account, 'zip'):
            print("Missing attribute zip")
            return True
        elif not hasattr(account, 'name') or not hasattr(account, 'id') or not hasattr(account, 'value'):
            print("Missing attribute name id or value")
            return True
        elif not isinstance(account.name, str):
            print("Account name is not a string")
            return True
        elif not isinstance(account.id, int):
            print("Account id is not a number")
            return True
        elif not isinstance(account.value, (int, float)):
            print("Account value is no a number")
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
        elif type(name) == Account:
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
        if len(accnt) % 2 == 0:
            if not hasattr(to_fix, 'extra'):
                setattr(to_fix, 'extra', 'optional')
            else:
                setattr(to_fix, 'extra2', 'optional too')
        return True
        
if __name__ == "__main__":
        
    bank = Bank()
#     john = Account(
#     'William John',
#     zip='100-064',
#     brother="heyhey",
#     value=6460.0,
#     ref='58ba2b9954cd278eda8a84147ca73c87',
#     info=None,
#     other='This is the vice president of the corporation',
#     lol = "hihi"
# )
    
#     john = Account(
#     'William John',
#     zip='100-064',
#     rother="heyhey",
#     value=6460.0,
#     ref='58ba2b9954cd278eda8a84147ca73c87',
#     info=None,
#     other='This is the vice president of the corporation',
# )

    # john = Account(
    #     'William John',
    #     zip='100-064',
    #     rother="heyhey",
    #     ref='58ba2b9954cd278eda8a84147ca73c87',
    #     info=None,
    #     other='This is the vice president of the corporation',
    #     lol = "lolilol",
    # )
    
    # acc1 = bank.add(john)
    # print(acc1)
    # print(john.name)
    # print(john.zip)
    # print(john.value)
    # print(bank.is_corrupted(john))
    # # print(bank.fix_account(john))
    # # print(bank.fix_account('William John'))
  
   
    jane = Account(
        'Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31')
    

    jhon = Account(
        'Jhon',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )

    bank.add(jhon)

    print("testing a valid transfer")
    print('1', jhon.value)
    print('2', jane.value)
    
    bank.transfer("Jhon", "Jane", 500)

    print('1', jhon.value)
    print('2', jane.value)