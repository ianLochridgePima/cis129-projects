# Author: Ian Lochridge
# This program takes in user input/orders and prints out a receipt

print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
numCoffees = float(input())  #converts input to a float for float multiplication
print("Number of muffins bought?")
numMuffins = float(input())  #converts input to a float for float multiplication
print("Number of pancakes bought?")
numPancakes = float(input())  #converts input to a float for float multiplication
print("Number of orange juices bought?")
numOrangeJuices = float(input())  #converts input to a float for float multiplication
print("***************************************")
print()
print("***************************************")
print("My Coffee and Muffin Shop Receipt")

coffeePrice = numCoffees * 5.00  #float multiplication, jupyter notebook errors for int*float
muffinPrice = numMuffins * 4.00  #float multiplication, jupyter notebook errors for int*float
pancakePrice = numPancakes * 7.00  #float multiplication, jupyter notebook errors for int*float
orangeJuicePrice = numOrangeJuices * 2.00  #float multiplication, jupyter notebook errors for int*float
orderPrice = coffeePrice + muffinPrice + pancakePrice + orangeJuicePrice  #before tax
taxPrice = orderPrice * 0.06
taxPriceString = str(taxPrice)  #string representation of tax, used to truncate off leading "0"
finalPrice = orderPrice + taxPrice  #after tax

if numCoffees > 1.0: #changes coffee to coffees when multiple are ordered
    print(int(numCoffees), " Coffees at $5 each: $ ", coffeePrice, "0", sep = "")  #sep used to add "0" at the end for double 0 price without a space between the 0s
else: 
    print(int(numCoffees), " Coffee at $5 each: $ ", coffeePrice, "0", sep = "")  #sep used to add "0" at the end for double 0 price without a space between the 0s

if numMuffins > 1.0: #changes muffin to muffins when multiple are ordered
    print(int(numMuffins), " Muffins at $4 each: $ ", muffinPrice, "0", sep = "")  #sep used to add "0" at the end for double 0 price without a space between the 0s
else: 
    print(int(numMuffins), " Muffin at $4 each: $ ", muffinPrice, "0", sep = "")  #sep used to add "0" at the end for double 0 price without a space between the 0s

if numPancakes > 1.0: #changes pancake to pancakes when multiple are ordered
    print(int(numPancakes), " Pancakes at $7 each: $ ", pancakePrice, "0", sep = "")  #sep used to add "0" at the end for double 0 price without a space between the 0s
else: 
    print(int(numPancakes), " Pancake at $7 each: $ ", pancakePrice, "0", sep = "")  #sep used to add "0" at the end for double 0 price without a space between the 0s
    
if numOrangeJuices > 1.0: #changes orange juice to orange juices when multiple are ordered
    print(int(numOrangeJuices), " Orange Juices at $2 each: $ ", orangeJuicePrice, "0", sep = "")  #sep used to add "0" at the end for double 0 price without a space between the 0s
else: 
    print(int(numOrangeJuices), " Orange Juice at $2 each: $ ", orangeJuicePrice, "0", sep = "")  #sep used to add "0" at the end for double 0 price without a space between the 0s
    
if taxPrice < 1: #truncates the leading 0 when tax amount is less than $1
    print("6% tax: $", taxPriceString[1:])
else:
    print("6% tax: $", taxPrice)
print("---------")

print("Total: $", finalPrice)
print("***************************************")
print("Thanks for visiting my shop. Have a good day!")
