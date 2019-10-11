#!/usr/bin/env python3

from bonkmod import Bank, Bankaccount

# Create a bank object
bonkbank   = Bank("Bonk Bank - Saves you(r) money")

# Create three bankaccount objects
johndoe        = Bankaccount("John Doe")
joesixpack     = Bankaccount("Joe Sixpack")
philanthropist = Bankaccount("Phil Anthropist", 50000.00)

# Add the bankaccounts to the bank:
bonkbank.openaccount(12345, johndoe)
bonkbank.openaccount(54321, joesixpack)
bonkbank.openaccount(67890, philanthropist)

# Handle transactions on the account:
bonkbank.transaction(67890, 12345, 3000.00)
bonkbank.transaction(67890, 54321,   50.00)
bonkbank.transaction(54321, 12345,   35.99)
bonkbank.transaction(54321, 12345,   25.00)

# Display all bank accounts of the Bonk Bank
print(bonkbank)

for account, accountinfo in bonkbank:
    print("%9d\t%s" % (account, accountinfo))
