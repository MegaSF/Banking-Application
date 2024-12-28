
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
        print(f"New checking total: ${PersonalCheck.total}\n")
        x = f"Amount deposited: {PersonalCheck.deposit}"
        with open("AccountHistoryChecking.txt", "a") as file:
            file.write(x + "\n")
    elif AccountChoice == "savings":
        PersonalSave.deposit = float(input("How much would you like to deposit?\n>"))
        PersonalSave.total += PersonalSave.deposit
        print(f"New savings total: {PersonalSave.total}")
        x = f"Amount deposited: {PersonalSave.deposit}"
        with open("AccountHistorySaving.txt", "a") as file:
            file.write(x + "\n")
    else:
        print("Invalid input. Please try again.")
        Deposit()

def Withdraw():
    AccountChoice = input("Would you like to withdraw from your [checking] [savings] account?\n>")
    if AccountChoice == "checking":
        PersonalCheck.withdraw = float(input("How much would you like to withdraw?\n>"))
        PersonalCheck.total -= PersonalCheck.withdraw
        print(f"New checking total: ${PersonalCheck.total}")
        x = f"Amount withdrawn: {PersonalCheck.withdraw}"
        with open("AccountHistoryChecking.txt", "a") as file:
            file.write(x + "\n")
    elif AccountChoice == "savings":
        PersonalSave.withdraw = float(input("How much would you like to withdraw?\n>"))
        PersonalSave.total -= PersonalSave.withdraw
        print(f"New savings total: {PersonalSave.total}")
        x = f"Amount withdrawn: {PersonalSave.withdraw}"
        with open("AccountHistorySaving.txt", "a") as file:
            file.write(x + "\n")
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
        x = f"Amount transferred: -{PersonalCheck.transfer}"
        with open("AccountHistoryChecking.txt", "a") as file:
            file.write(x + "\n")
        y = f"Amount transferred: +{PersonalCheck.transfer}"
        with open("AccountHistorySaving.txt", "a") as file:
            file.write(y + "\n")
    elif AccountChoice == "savings":
        PersonalSave.transfer = float(input("How much would you like to transfer?\n>"))
        PersonalSave.total -= PersonalSave.transfer
        PersonalCheck.total += PersonalSave.transfer
        print(f"New Savings total: ${PersonalSave.total}")
        print(f"New Checking total: ${PersonalCheck.total}")
        y = f"Amount transferred: -{PersonalSave.transfer}"
        with open("AccountHistorySaving.txt", "a") as file:
            file.write(y + "\n")
        x = f"Amount transferred: +{PersonalSave.transfer}"
        with open("AccountHistoryChecking.txt", "a") as file:
            file.write(x + "\n")
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


BankActions = {
    "1" : ViewAccounts,
    "2" : Deposit,
    "3" : Withdraw,
    "4" : Transfer,
    "5" : SaveAccounts,
    "6" : LoadAccounts,
    "7" : Quit
}