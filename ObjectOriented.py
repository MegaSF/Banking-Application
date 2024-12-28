#Evan Rhea                  11-21-2024
# Simple Bank Account Application

# We import EVERYTHING from bank acct errors and extra01 for ease of use, everything they contain is useful,
# applicable, or otherwise necessary for this project to function. Their inclusion also keeps this code shorter and easier to read
# (for the most part)
from ExtraOne import *
from BankAccountErrors import *

#this is a personal bank account app that focuses on the idea of object oriented programming in python via classes
#It sports a parant general bank account, which well treat as a sortof interrealm or inbetween for savings and checking
#it uses functions for trasnfering, withdrawing, and viewing accounts

#Phases commented in along with a "TODO" comment, explainign what needs to be done or is done (marked with a [DONE] tag)
#Project will be updated more and more, eventually could be used for official banking actions as main goal (wont be, but fun to imagine)

PersonalAccount = BankAccount(total=None, deposit=0, transfer=0, withdraw=0)
#Set a base total to play around with
PersonalAccount.total = 0.00

#Creates objects to access info/data in checking and savings accounts respectively
PersonalSave = SavingsAccount(total=0, deposit=0, transfer=0, withdraw=0)
PersonalCheck = CheckingAccount(total=0, deposit=0, transfer=0, withdraw=0)


# PHASE 1
# [DONE] (TODO: build a system that allows user to either [VIEW] accounts, or [QUIT] the application)

# Phase 2
# [DONE] (TODO: Create system for depositing money into an account)

# Phase 3
# [DONE] (TODO: Create a system that allows the user to transfer funds between accounts, and results in an error if there isn't enough money
# to complete the transaction/transfer)

# Phase 4
# [DONE] (TODO: Create a method to withdraw funds from an account)

# Phase 5
# [DONE] (TODO:(Paper statement printing)

# Phase 6
# [DONE] (TODO: Fix small bugs/functions)
#   6a.) Transfer too nay funds [DONE]
#   6b.) Cannot withdraw too many funds [DONE]
#   6c.) Remove ability to withdraw from savings [DONE]

# Phase 7
# [DONE] (TODO: Add more code documentation, should be able to have
# reason for EVERY LINE, if there isn't a good enough reason to keep it,
# remove it (may need more review later lol))

# Phase 7.5
# [DONE] (TODO: Document Class and error files)

# Phase 8
# TODO: Create system for customers to save and load data into application


#Application runtime startup
running = True
while running:
    # Create object of customer wallet, plan to remove unless use is found
    CustomerWallet = 500.25
    try:
        #Main menu for user to navigate between account functionality or quitting out of said application
        MainMenuUser = input("Would you like to [VIEW] accounts, make a [DEPOSIT], [TRANSFER] funds between accounts, [WITHDRAW] funds,get a [PAPER] statement, [SAVE] user data, [LOAD] user data, or [QUIT] the application?\n> ").upper().strip()

# Start of [VIEW] segment
        if MainMenuUser == "VIEW":
            # A user should have easy access to view account information, in case something goes awry
            # Accomplished via print statements + custom formatting
            AccountChoice = input("Would you like to view:\n[SAVINGS]   [TOTAL]    [CHECKING]\n> ").upper().strip()
            if AccountChoice == "CHECKING":
                PersonalCheck.PrintChecking()
            elif AccountChoice == "SAVINGS":
                PersonalSave.PrintSaving()
            elif AccountChoice == "TOTAL":
                PersonalAccount.PrintInformation()
            else:
                # Preventative measure to stop user from entering bad input (account doesnt exist, etc.)
                print("Bad input... Returning to menu...")
# End of [VIEW] segment
        
# Start of [DEPOSIT] segment
        elif MainMenuUser == "DEPOSIT":
            AccountSelect = input("Would you like to deposit to:\n[SAVINGS]   [TOTAL]    [CHECKING]\n> ").upper().strip()
            # If/elif blocks to get initial account, meant for user to pre select an account
            if AccountSelect == "SAVINGS":
                PersonalSave.deposit = float(input("Please enter an amount to deposit into your account:\n> "))
                try:
                    # Helps with catching numbers <0, not much more to say
                    if PersonalSave.deposit <= 0:
                        print("Money to deposit must be greater than 0")
                    else:
                        PersonalSave.Savingtotal += PersonalSave.deposit
                except Exception as ToolittleDepo:
                    print("ERROR: Bad input")
            elif AccountSelect == "TOTAL":
                PersonalAccount.deposit = float(input("Please enter an amount to deposit into your account:\n> "))
                try:
                    if PersonalAccount.deposit <= 0:
                        print("Money to deposit must be greater than 0")
                    else:
                        PersonalAccount.total += PersonalAccount.deposit
                except Exception as ToolittleDepo:
                    print("ERROR: Deposit amount too low")
            elif AccountSelect == "CHECKING":
                PersonalCheck.deposit = float(input("Please enter an amount to deposit into your account:\n> "))
                try:
                    if PersonalCheck.deposit <= 0:
                        print("Money to deposit must be greater than 0")
                    else:
                        PersonalCheck.Checkingtotal += PersonalCheck.deposit
                except Exception as ToolittleDepo:
                    print("ERROR: Bad input")
            else:
                # Once again catching bad inputs
                raise BadUserInput(AccountSelect)
# End of [DEPOSIT] segment

# Start of [TRANSFER] segment
        elif MainMenuUser == "TRANSFER":
            AccountSelect = input("Which account you like to transfer money from:\n[SAVINGS]   [TOTAL]    [CHECKING]\n> ").upper().strip()
            if AccountSelect == "SAVINGS":
                try:
                    TransferAmount = float(input("Please enter an amount to transfer into another account:\n> "))
                    SecondAccountSelect = input("Which account you like to transfer money to:\n[TOTAL]    [CHECKING]\n> ").upper().strip()
                    if TransferAmount > AccountSelect:
                        raise InsufficientFunds()
                    if SecondAccountSelect == "CHECKING":
                        # We use the objects and set them equal to the transfer amount here in order to better
                        # keep totals accurately calculated, assigned on same line for efficiency, repeated
                        # for other accounts
                        PersonalSave.transfer, PersonalCheck.transfer = TransferAmount, TransferAmount
                        PersonalSave.Savingtotal -= PersonalSave.transfer
                        PersonalCheck.Checkingtotal += PersonalCheck.transfer
                        print(f"Transferred {TransferAmount} from SAVINGS to CHECKING")
                    elif SecondAccountSelect == "TOTAL":
                        PersonalSave.transfer, PersonalAccount.transfer = TransferAmount, TransferAmount
                        PersonalSave.Savingtotal -= PersonalSave.transfer
                        PersonalAccount.total += PersonalAccount.transfer
                        print(f"Transferred {TransferAmount} from SAVINGS to TOTAL")
                except Exception as e:
                    print("ERROR! Too little funds!")
            elif AccountSelect == "TOTAL":
                try:
                    TransferAmount = float(input("Please enter an amount to transfer into another account:\n> "))
                    SecondAccountSelect = input("Which account you like to transfer money to:\n[SAVINGS]    [CHECKING]\n> ").upper().strip()
                    if TransferAmount > AccountSelect:
                            raise InsufficientFunds()
                    if SecondAccountSelect == "CHECKING":
                        PersonalAccount.transfer, PersonalCheck.transfer = TransferAmount, TransferAmount
                        PersonalAccount.total -= PersonalAccount.transfer
                        PersonalCheck.Checkingtotal += PersonalCheck.transfer
                        print(f"Transferred {TransferAmount} from TOTAL to CHECKING")
                    elif SecondAccountSelect == "SAVINGS":
                        PersonalSave.transfer, PersonalAccount.transfer = TransferAmount, TransferAmount
                        PersonalAccount.total -= PersonalAccount.transfer
                        PersonalSave.Savingtotal += PersonalSave.transfer
                        print(f"Transferred {TransferAmount} from TOTAL to SAVINGS")
                except Exception as e:
                    print("ERROR! Too little funds!")
            elif AccountSelect == "CHECKING":
                try:
                    TransferAmount = float(input("Please enter an amount to transfer into another account:\n> "))
                    SecondAccountSelect = input("Which account you like to transfer money to:\n[TOTAL]    [SAVINGS]\n> ").upper().strip()
                    if TransferAmount > AccountSelect:
                            raise InsufficientFunds()
                    if SecondAccountSelect == "TOTAL":
                        PersonalAccount.transfer, PersonalCheck.transfer = TransferAmount, TransferAmount
                        PersonalCheck.Checkingtotal -= PersonalCheck.transfer
                        PersonalAccount.total += PersonalAccount.transfer
                        print(f"Transferred {TransferAmount} from CHECKING to TOTAL")
                    elif SecondAccountSelect == "SAVINGS":
                        PersonalSave.transfer, PersonalCheck.transfer = TransferAmount, TransferAmount
                        PersonalCheck.Checkingtotal -= PersonalCheck.transfer
                        PersonalSave.Savingtotal += PersonalSave.transfer
                        print(f"Transferred {TransferAmount} from CHECKING to SAVINGS")
                except Exception as e:
                    print("ERROR! Too little funds!")
            else:
                raise BadUserInput(AccountSelect)
# End of [TRANSFER] segment
            
# Start of [WITHDRAW] segment
        elif MainMenuUser == "WITHDRAW":
            AccountSelect = input("Please select account to withdraw from:\n[TOTAL]    [CHECKING]\n> ").strip().upper()
            try:
                if AccountSelect == "TOTAL":
                    WithDrawAmount = float(input("Please select amount to withdraw from SAVINGS:\n> "))
                    if WithDrawAmount > PersonalAccount.total:
                        raise InsufficientFunds()
                    PersonalAccount.withdraw = WithDrawAmount
                    PersonalAccount.total -= PersonalAccount.withdraw
                    print(f"Withdrew: ${PersonalAccount.withdraw} from TOTAL")
                elif AccountSelect == "CHECKING":
                    WithDrawAmount = float(input("Please select amount to withdraw from SAVINGS:\n> "))
                    if WithDrawAmount > PersonalCheck.Checkingtotal:
                        raise InsufficientFunds()
                    PersonalCheck.withdraw = WithDrawAmount
                    PersonalCheck.Checkingtotal -= PersonalCheck.withdraw
                    print(f"Withdrew: ${PersonalCheck.withdraw} from CHECKING")
                else:
                    raise BadUserInput
            except Exception as e:
                print("ERROR! Insufficient Funds")
# End of [WITHDRAW] segment
            
# Start of [PAPER] segment (maybe change to receipt?)
        elif MainMenuUser == "PAPER":
            AccountChoice = input("Please select accuont to make paper statement for:\n[SAVINGS]   [TOTAL]    [CHECKING]\n> ").upper().strip()
            if AccountChoice == "CHECKING":
                PersonalCheck.CheckingPaperStatement()
            elif AccountChoice == "SAVINGS":
                PersonalSave.SavingsPaperStatement()
            elif AccountChoice == "TOTAL":
                PersonalAccount.TotalPaperStatement()
            else:
                print("Bad input... Returning to menu...")
# End of [PAPER] segment

# Start of [SAVE] statement
        elif MainMenuUser == "SAVE":
            Username = input("Please enter customer username:\n")
            Password = input("Please enter a password:\n")
            data = {"name" : Username,
                    "password" : Password,
                    "CustomSave" : PersonalSave.Savingtotal,
                    "CustomCheck" : PersonalCheck.Checkingtotal,
                    "PersonalGen" : PersonalAccount.total
                    }
            data = json.dumps(data)
            AccountName = Username + Password
            with open(AccountName + ".json", "w") as outfile:
                json.dump(data, outfile)
# End of [SAVE] segment

# Start of [LOAD] segment
        elif MainMenuUser == "LOAD":
            try:
                UserFile = input("Please enter username + password (no space in between):\n") + ".json"
                with open(UserFile) as infile:
                    UserJSONdata = json.load(infile)
                    BankingInfo = json.loads(UserJSONdata)
                    PersonalAccount.total = BankingInfo["PersonalGen"]
                    PersonalCheck.Checkingtotal = BankingInfo["CustomCheck"]
                    PersonalSave.Savingtotal = BankingInfo["CustomSave"]
            except Exception:
                print("File not found")

        elif MainMenuUser == "QUIT":
            #Quitting application
            print("Quitting application...")
            running = False
        else:
            #Created custom error to handle bad input
            raise BadUserInput(MainMenuUser)

    except Exception as errormsgUser:
        #Basic error msg, can be ignored or altered, but good for practice
        print(f"ERROR: Invalid Input!")
        print(f"Entered: {errormsgUser}")