# Evan Rhea                12-28-2024
from Functions import *
def main():
    running = True
    while running:
        MainMenu()
        MenuOpt = input("> ")
        action = BankActions.get(MenuOpt)
        if action:
            action()
        else:
            print("Error, action not found!")
            print("Try just selecting the number?")
if __name__ == "__main__":
    main()