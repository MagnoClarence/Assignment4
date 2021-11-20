# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def userInputs():
    firstInput = float(input("Enter 1st number: "))
    secondInput = float(input("Enter 2nd number: "))
    thirdInput = float(input("Enter 3rd number: "))
    fourthInput = float(input("Enter 4th number: "))
    return firstInput, secondInput, thirdInput, fourthInput

order = userInputs()

# I followed the tournament system where i make them compete with each other first then
# Compare the winners and losers to each other in order to find the order

# First Round or Semi-Finals
if order[0] >= order[1]:
    finalistOne = order[0]
    matchOneLose = order[1]
else:
    finalistOne = order[1]
    matchOneLose = order[0]
if order[2] >= order[3]:
    finalistTwo = order[2]
    matchTwoLose = order[3]
else:
    finalistTwo = order[3]
    matchTwoLose = order[2]
if matchOneLose >= matchTwoLose: # I compared the two losers from the first round to find whose third and fourth
    third = matchOneLose
    fourth = matchOneLose
else:
    third = matchTwoLose
    fourth = matchOneLose

#Finals
if finalistOne >= finalistTwo:
    first = finalistOne
    second = finalistTwo
else:
    first = finalistTwo
    second= finalistOne

# Print the order from highest to lowest
list = [first,second,third,fourth]
print(list)

