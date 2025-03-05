# Lab 5 The Bottle Return Program 
# Ian Lochridge 
# 3/4/25 
# This program tracks collected bottles and calculates their value

# Declare variables below 
totalBottles = 0
todayBottles = 0
totalPayout = 0
counter = 1
keepGoing = 'y'
PAYOUT_PER_BOTTLE = 0.10
NBR_OF_DAYS = 7

while keepGoing == 'y': #allow the user to input multiple weeks of data
    totalPayout = 0
    totalBottles = 0
    for counter in range(NBR_OF_DAYS): #collect each day's data
        todayBottles = int(input(f'Enter number of bottles for day #{counter+1}:'))
        totalBottles = totalBottles + todayBottles
        
    # print the number of total bottles and total payout
    print ("The total number of bottles collected is", totalBottles) 
    totalPayout = totalBottles*PAYOUT_PER_BOTTLE
    print ("The total paid out is $", totalPayout)
    Input = input('Do you want to enter another week’s worth of data? (Enter y or n):') #repeat or exit the loop
    if Input != 'y':
        break
