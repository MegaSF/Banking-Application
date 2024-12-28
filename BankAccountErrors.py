#Evan Rhea                  11-21-2024
# Simple Bank Account Application errors

from ExtraOne import *
# Import items from class file in case there are niche or hyper
# specific errors we need to be able to catch, at base two errors, one for bad input 
# and one for insufficient funds

class InsufficientFunds(Exception):
    def __init__(self, transfer, total):
        self.transfer = transfer
        self.total = total

class BadUserInput(Exception):
    def __init__(self, userinput):
        self.userinput = userinput