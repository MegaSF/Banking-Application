# Evan Rhea             12-23-2024
# This is an updated version of the ObjectOriented.py file. This version focuses on the refactoring that copilot offered.

from ExtraOne import *
from BankAccountErrors import *

#Creates objects to access info/data in checking and savings accounts respectively
PersonalSave = SavingsAccount(total=0, deposit=0, transfer=0, withdraw=0)
PersonalCheck = CheckingAccount(total=0, deposit=0, transfer=0, withdraw=0)


# This is the [VIEW] function that allows the user to view their account balances. We use this as a way to check the status of the account.
# That way we can see if the deposit, transfer, or withdraw functions are working properly.


def ViewAccounts():
    AccountChoice = input("Would you like to view your [checking] [savings] account?\n>")
    if AccountChoice == "checking":
        print(f"Checking total: ${PersonalCheck.total}")
        
    elif AccountChoice == "savings":
        print(f"Savings total: ${PersonalSave.total}")
    else:
        print("Invalid input. Please try again.")
        ViewAccounts()

# This is the [DEPOSIT] function that allows the user to deposit money into their account. We use this as a way to add money to the account.

def Deposit():
    AccountChoice = input("Would you like to deposit into your [checking] [savings] account?\n>")
    if AccountChoice == "checking":
        PersonalCheck.deposit = float(input("How much would you like to deposit?\n>"))
        PersonalCheck.total += PersonalCheck.deposit
        print(f"New checking total: ${PersonalCheck.total}")
    elif AccountChoice == "savings":
        PersonalSave.deposit = float(input("How much would you like to deposit?\n>"))
        PersonalSave.total += PersonalSave.deposit
        print(f"New savings total: {PersonalSave.total}")
    else:
        print("Invalid input. Please try again.")
        Deposit()

def Withdraw():
    AccountChoice = input("Would you like to withdraw from your [checking] [savings] account?\n>")
    if AccountChoice == "checking":
        PersonalCheck.withdraw = float(input("How much would you like to withdraw?\n>"))
        PersonalCheck.total -= PersonalCheck.withdraw
        print(f"New checking total: ${PersonalCheck.total}")
    elif AccountChoice == "savings":
        PersonalSave.withdraw = float(input("How much would you like to withdraw?\n>"))
        PersonalSave.total -= PersonalSave.withdraw
        print(f"New savings total: {PersonalSave.total}")
    else:
        print("Invalid input. Please try again.")
        Withdraw()

def Transfer():
    AccountChoice = input("Would you like to transfer from your [checking] [savings] account?\n>")
    if AccountChoice == "checking":
        PersonalCheck.transfer = float(input("How much would you like to transfer?\n>"))
        PersonalCheck.total -= PersonalCheck.transfer
        PersonalSave.total += PersonalCheck.transfer
        print(f"New Checking total: ${PersonalCheck.total}")
        print(f"New Savings total: ${PersonalSave.total}")
    elif AccountChoice == "savings":
        PersonalSave.transfer = float(input("How much would you like to transfer?\n>"))
        PersonalSave.total -= PersonalSave.transfer
        PersonalCheck.total += PersonalSave.transfer
        print(f"New Savings total: ${PersonalSave.total}")
        print(f"New Checking total: ${PersonalCheck.total}")
    else:
        print("Invalid input. Please try again.")
        Transfer()


def SaveAccounts():
    Username = input("Please enter customer username:\n")
    Password = input("Please enter a password:\n")
    data = {"name" : Username,
            "password" : Password,
            "CustomSave" : PersonalSave.total,
            "CustomCheck" : PersonalCheck.total
            }
    data = json.dumps(data)
    AccountName = Username + Password
    with open(AccountName + ".json", "w") as outfile:
        json.dump(data, outfile)

def LoadAccounts():
    try:
        UserFile = input("Please enter username + password (no space in between):\n") + ".json"
        with open(UserFile) as infile:
            UserJSONdata = json.load(infile)
            BankingInfo = json.loads(UserJSONdata)
            
            PersonalCheck.total = BankingInfo["CustomCheck"]
            PersonalSave.total = BankingInfo["CustomSave"]
    except Exception:
        print("File not found")

def Quit():
    print("Goodbye!")
    exit()





def main():
    running = True
    while running:
        MainMenu()
        try:
            menuChoice = input("Please enter a choice: ")
            if menuChoice == "1":
                ViewAccounts()
            elif menuChoice == "2":
                Deposit()
            elif menuChoice == "3":
                Withdraw()
            elif menuChoice == "4":
                Transfer()
            elif menuChoice == "5":
                SaveAccounts()
            elif menuChoice == "6":
                LoadAccounts()
            elif menuChoice == "7":
                Quit()
            else:
                print("Invalid input. Please try again.")
        except Exception as e:
            print("Error occured!")
            print("Error msg: ", e)

if __name__ == "__main__":
    main()