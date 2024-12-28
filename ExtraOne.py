#Evan Rhea                  11-21-2024
# Simple Bank Account Application classes        

import json
from Menu import *

# We create a bank accou nt parent class that serves as a mold for any and ALL
# other bank accounts initially made or to be made in future
class BankAccount:
    def __init__(self, total, deposit, transfer, withdraw):
        self.total = total
        self.deposit = deposit
        self.transfer = transfer
        self.withdraw = withdraw

    # We use this function to give users the ability to 
    # keep an eye on their account
    def PrintInformation(self):
        print(f"BANK ACCOUNT INFORMATION:")
        print("-"*25)
        print(f"TOTAL:\t${self.total:.2f}")
        print(f"DATE CREATED:\t11-21-2024")
    
    # We use this function to generate receipts for users
    def TotalPaperStatement(self):
        print(f"    RHEATECH BANKING")
        print("-"*24)
        print(f"    TOTAL ACCOUNT")
        print(f"\t${self.total}")
        print(f"DATE CREATED:\t11-21-2024")

# Savings class, acts as "parent" for others, will hold withdraw statement with no value associated
# parent for new savings accounts
class SavingsAccount(BankAccount):
    def __init__(self, total, deposit, transfer, withdraw):
        super().__init__(total, deposit, transfer, withdraw)
        self.Savingtotal = (total + deposit - transfer - withdraw)
    
    def PrintSaving(self):
        print(f"SAVINGS ACCOUNT INFORMATION:")
        print("-"*25)
        print(f"TOTAL:\t${self.Savingtotal:.2f}")
        print(f"DATE CREATED:\t11-21-2024")

    def SavingsPaperStatement(self):
        print(f"    RHEATECH BANKING")
        print("-"*24)
        print(f"    SAVINGS ACCOUNT")
        print(f"\t${self.Savingtotal}")
        print(f"DATE CREATED:\t11-21-2024")

# Checking class, acts as "parent" of future checking accounts
class CheckingAccount(BankAccount):
    def __init__(self, total, deposit, transfer, withdraw):
        super().__init__(total, deposit, transfer, withdraw)
        self.Checkingtotal = (total + deposit - transfer - withdraw)

    def PrintChecking(self):
        print(f"CHECKING ACCOUNT INFORMATION:")
        print("-"*25)
        print(f"TOTAL:\t${self.Checkingtotal:.2f}")
        print(f"DATE CREATED:\t11-21-2024")

    def CheckingPaperStatement(self):
        print(f"    RHEATECH BANKING")
        print("-"*24)
        print(f"    CHECKING ACCOUNT")
        print(f"\t${self.Checkingtotal}")
        print(f"DATE CREATED:\t11-21-2024")