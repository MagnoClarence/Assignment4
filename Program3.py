# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.

def getInput():
    """takes an input and returns a value depending on the parameter requested
    
        arg: dataIn - a string that determines the output value
        return: a value from the userInput
        
    """
    # ask the user for how much money they have and how much an apple is.
    while 1:
        money = int(input("How much money do you have?: "))
        appleCost = int(input("How much is an apple?: "))
        
        if money < 0 and appleCost < 0:
            print("You cannot input negative number.")
        else:
            break
    return money, appleCost

print("program 3")

bill = getInput()

# Show the user how many apples they can buy with their money and the change they will get if they have one.
while 1:
    if bill[0] >= bill[1]:
        print(f"you can buy {int(bill[0] / bill[1])} apple(s) and your change is ₱{bill[0]%bill[1]}")
        break
    else:
        print(f"you cannot afford an apple. You are missing P{bill[1] - bill[0]}")
        bill = getInput()