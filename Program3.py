# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.

def getInput(dataIn):
    """takes an input and returns a value depending on the parameter requested
    
        arg: dataIn - a string that determines the output value
        return: a value from the userInput
        
    """
    while 1:
        if dataIn == "money":
            bill = int(input("How much money do you have?: "))
        else:
            bill = int(input("How much is an apple?: "))
        if bill < 0:
            print("You cannot input negative number.")
        else:
            break
    return bill

print("program 3")
money = getInput("money")
appleCost = getInput("appleCost")

while 1:
    if money >= appleCost:
        print(f"you can buy {int(money / appleCost)} apple(s) and your change is ₱{money%appleCost}")
        break
    else:
        print(f"you cannot afford an apple. You are missing P{appleCost - money}")
        money = getInput("money")
    
exit()