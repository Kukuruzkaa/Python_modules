from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    jane = bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
        
    ))
    john = bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87'
        # info=None
    ))

    print(jane)
    print(john)
    
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')

        print("john corrupted before", bank.is_corrupted('William John'))
        print("jane corrupted before", bank.is_corrupted('Smith Jane'))
        print("fix john",bank.fix_account('William John'))
        print("fix jane", bank.fix_account('Smith Jane'))

        print("john corrupted after fix", bank.is_corrupted('William John'))
        print("jane corrupted after fix", bank.is_corrupted('Smith Jane'))
        
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
    else:
        print('Success')
