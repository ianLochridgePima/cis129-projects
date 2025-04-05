# CIS129
# Ian Lochridge
# 4/4/25
# This program collects seats sold in a theatre and calculates income generated

def main():
    # define section names
    SECTION_A_NAME = "Section A"
    SECTION_B_NAME = "Section B"
    SECTION_C_NAME = "Section C"

    # define amount of seats available and seat cost
    SECTION_A_SEAT_COST = 20  
    SECTION_B_SEAT_COST = 15  
    SECTION_C_SEAT_COST = 10  

    SECTION_A_TOTAL_SEATS = 300  
    SECTION_B_TOTAL_SEATS = 500  
    SECTION_C_TOTAL_SEATS = 200  
    MINIMUM_SEATS_SOLD = 0

    # define # of seat purchases
    sectionASeatPurchases = 0 
    sectionBSeatPurchases = 0
    sectionCSeatPurchases = 0

    # define income generated from each section and total income
    sectionAIncome = 0
    sectionBIncome = 0
    sectionCIncome = 0
    totalIncome = 0

    # print seats available and seat cost
    print()
    print("Welcome to the Dramatic Theatre:")
    print()
    print(f"{SECTION_A_NAME} Seats Available:", SECTION_A_TOTAL_SEATS)
    print(f"{SECTION_B_NAME} Seats Available:", SECTION_B_TOTAL_SEATS)
    print(f"{SECTION_C_NAME} Seats Available:", SECTION_C_TOTAL_SEATS)
    print()
    print(f"{SECTION_A_NAME} Seat Cost:", SECTION_A_SEAT_COST)
    print(f"{SECTION_B_NAME} Seat Cost:", SECTION_B_SEAT_COST)
    print(f"{SECTION_C_NAME} Seat Cost:", SECTION_C_SEAT_COST)


    sectionASeatPurchases = gatherUserInput(MINIMUM_SEATS_SOLD, SECTION_A_TOTAL_SEATS, SECTION_A_NAME)  #collect seats sold for section A
    sectionAIncome = calculateIncome(sectionASeatPurchases, SECTION_A_SEAT_COST)  #calculate section A income
    totalIncome = totalIncome + sectionAIncome  #update total income w/ section A income
    print()
    print(f"{SECTION_A_NAME} Seats Purchased:", sectionASeatPurchases)  #display seats sold
    print("Subtotal:", totalIncome)  #display current total income

    sectionBSeatPurchases = gatherUserInput(MINIMUM_SEATS_SOLD, SECTION_B_TOTAL_SEATS, SECTION_B_NAME)  #collect seats sold for section B
    sectionBIncome = calculateIncome(sectionBSeatPurchases, SECTION_B_SEAT_COST)  #calculate section B income
    totalIncome = totalIncome + sectionBIncome  #update total income w/ section B income
    print()
    print(f"{SECTION_B_NAME} Seats Purchased:", sectionBSeatPurchases)  #display seats sold
    print("Subtotal:", totalIncome)  #display current total income

    sectionCSeatPurchases = gatherUserInput(MINIMUM_SEATS_SOLD, SECTION_C_TOTAL_SEATS, SECTION_C_NAME)  #collect seats sold for section C
    sectionCIncome = calculateIncome(sectionCSeatPurchases, SECTION_C_SEAT_COST)  #calculate section C income
    totalIncome = totalIncome + sectionCIncome  #update total income w/ section C income
    print()
    print(f"{SECTION_C_NAME} Seats Purchased:", sectionCSeatPurchases)  #display seats sold
    print("Subtotal:", totalIncome)  #display current total income

    displayResults(sectionAIncome, sectionASeatPurchases, SECTION_A_NAME)  #call final display function for section A
    displayResults(sectionBIncome, sectionBSeatPurchases, SECTION_B_NAME)  #call final display function for section B
    displayResults(sectionCIncome, sectionCSeatPurchases, SECTION_C_NAME)  #call final display function for section C
    print("Total Income:", totalIncome)
    print()


def gatherUserInput(minValue, maxValue, sectionName):
    #gather the number of seats sold in each section
    print()
    print(f"Enter # of {sectionName} Seats:")  #display current section

    seats = int(input(""))  #collect seats sold

    while seats < minValue or seats > maxValue:  #input validation
        print()
        print("Invalid Value")  #display invalid value
        print(f"Enter # of {sectionName} Seats:")  #display currect section
        seats = int(input(""))  #recollect seats sold

    return seats  #return seats sold


def calculateIncome(seatPurchases, seatCost):
    return seatPurchases * seatCost  #calculate section income by multiplying seats purchased and seat cost


def displayResults(sectionIncome, sectionSeatPurchases, sectionName):
    #print out final values
    print()
    print(f"{sectionName} Seats:", sectionSeatPurchases)  #print section seats sold
    print(f"{sectionName} Income:", sectionIncome)  

main()

