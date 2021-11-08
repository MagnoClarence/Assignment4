#Clarence Magno
#program 2
#Nov 8, 2021

    # Create a program that will ask how many apples and oranges you want to buy.
    # Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
    
    # Constant values so that changing the price will be easy
APPLE_PRICE = 20
ORANGE_PRICE = 25
def fruitPrice():  
    applePrice = print(f"₱{APPLE_PRICE} per 1 piece of apple")
    orangePrice = print(f"₱{ORANGE_PRICE} per 1 piece of orange\n")
    return applePrice, orangePrice

def getQty(): 
    while 1:
        apples = int(input("How many apples do you want to buy?: "))
        oranges = int(input("How many oranges do you want to buy?: "))
        if apples >= 0 and oranges >= 0:
            break
        else:
            print("You cannot have negative fruits")
    return apples, oranges

def qtyBought():
    appleBought = print(f"Apples: \n qty: {fruitCnt[0]} \n price: ₱{fruitCnt[0] * APPLE_PRICE}")
    print ("\n")     
    orangesBought = print(f"Oranges: \n qty: {fruitCnt[1]} \n price: ₱{fruitCnt[1] * ORANGE_PRICE}") 
    return appleBought, orangesBought
        
print("program 2\n")

    #Step 1: Show how much 1 piece of apple and 1 piece of orange cost.
applePrice, orangePrice = fruitPrice()

    # Step 2: Ask the user how many apples do they plan to buy.
    # Step 3: Ask the user how many oranges do they plan to buy.
#applesCnt = getQty("apples")
#orangeCnt = getQty("oranges")
fruitCnt = getQty()

print("\n")

    # Show how many apple and oranges they bought and the total price for each fruit.
applesBought, orangesBought = qtyBought()

    # Final Step: Display the output in the following format. "The total amount is ______."
print("\n")
print(f"the total amount is ₱{(fruitCnt[0] * APPLE_PRICE) + (fruitCnt[1] * ORANGE_PRICE)}")
exit