def opening():
    print("#####################################")
    print("Welcome to the investment quote system")
    print("\nPlease enter your name")
    opening.name = input()
    print("Please enter your Address")
    opening.address = input()
    print("Please enter your telephone number")
    opening.phone = input()
    while not (opening.phone.isdigit() and len(opening.phone) == 11):
        print("not a valid phone number. please try again.")
        opening.phone = input()

    print("How much would you like to invest per month (£)?")
    opening.investSum = input()
    while not opening.investSum.isdecimal():
        print("please enter a number.")
        opening.investSum = input()

    opening.investSum = float(opening.investSum)

StopAsyncIteration
def options():
    print("#####################################")
    print("There are two types of investment available:")
    print("Option 1 - Savings plan")
    print("Option 2 - Managed stock investment")
    print("Please select an option (press 1 or 2 followed by enter)")
    print("#####################################")
    option = input()
    while option != "1" and option != "2":
        print("Please select an option (press 1 or 2 followed by enter)")
        option = input()
        
    if option == "1":
        savingsMain()

    else:
        stocksMain()

def savingsMain():
    savingsMain.monthlyInvest = opening.investSum
    savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12
    while savingsMain.yearlyInvest > 20000:
        print("The the initial monthly amount is too high for this type of plan.")
        print("How much would you like to invest per month (£)?")
        savingsMain.monthlyInvest = float(input())
        savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12
    
    savingsPrint()

def savingsMin():
    predictReturns = 0.012
    yearlyFees = 0.0025 * 12
    savingsMin.total = savingsMain.yearlyInvest
    print("#####################################")   
    print("Forecasted perfromance of this plan at the lowest rate of return:")
    for i in range(10):
        savingsMin.total = (savingsMin.total + (savingsMin.total * predictReturns)) - yearlyFees
        savingsMin.total = round(savingsMin.total, 2)
        if i == 1 or i == 5 or i == 10:
            print(f"At the end of year {i}")
            print("Your investment will be worth:")
            print(f"£{savingsMin.total}")
            print(f"\nTotal fees paid in this period: £{yearlyFees * (i+1)}")
            print(f"\nTotal profit in this period: £{savingsMin.total - (yearlyFees * (i+1))}")

    print("\n#####################################\n")

def savingsMax():
    predictReturns = 0.024
    yearlyFees = 0.0025 * 12
    savingsMax.total = savingsMain.yearlyInvest
    print("#####################################")
    print("Forecasted perfromance of this plan at the highest rate of return:")
    for i in range(10):
        savingsMax.total = (savingsMax.total + (savingsMax.total * predictReturns)) - yearlyFees
        savingsMax.total = round(savingsMax.total, 2)
        if i == 0 or i == 4 or i == 9:
            print("At the end of year", str(i+1))
            print("Your investment will be worth:")
            print(f"£{savingsMax.total}")
            print(f"\nTotal fees paid in this period: £{round(yearlyFees * (i+1), 2)}")
            print(f"\nTotal profit in this period: £{round(savingsMax.total - (yearlyFees * (i+1)), 2)}")

    print("\n#####################################\n")  

def stocksMain():
    stocksMain.monthlyInvest = opening.investSum
    stocksMain.yearlyInvest = stocksMain.monthlyInvest * 12
    stocksPrint()
    
def stocksMin():
    predictReturns = 0.04
    yearlyFees = 0.13 * 12
    stocksMin.total = stocksMain.yearlyInvest
    print("#####################################")
    print("Forecasted perfromance of this plan at the lowest rate of return:")
    for i in range(10):
        stocksMin.total = (stocksMin.total + (stocksMin.total * predictReturns)) - yearlyFees
        stocksMin.total = round(stocksMin.total, 2)
        if stocksMin.total >= 40000:
            taxRate = 0.2

        elif stocksMin.total >= 12000:
            taxRate = 0.1

        else:
            taxRate = 0
        
        taxPayable = stocksMin.total * taxRate
        postTax = stocksMin.total - taxPayable
        postTax = round(postTax, 2)
        if i == 0 or i == 4 or i == 9:
            print(f"At the end of year {i+1})")
            print("Your investment will be worth:")
            print(f"£{postTax}")
            print(f"\nTotal fees paid in this period: £{yearlyFees * (i+1)}")
            print(f"\nTotal profit in this period: £{postTax - (yearlyFees * (i+1))}")
            print(f"\nTotal tax due in this period: £{taxPayable}")

    print("\n#####################################\n")

def stocksMax():
    predictReturns = 0.23
    yearlyFees = 0.13 * 12
    stocksMax.total = stocksMain.yearlyInvest
    print("#####################################")
    print("Forecasted perfromance of this plan at the higher rate of return:")
    for i in range(10):
        stocksMax.total = (stocksMax.total + (stocksMax.total * predictReturns)) - yearlyFees
        stocksMax.total = round(stocksMax.total, 2)
        if stocksMax.total >= 40000:
            taxRate = 0.2

        elif stocksMax.total >= 12000:
            taxRate = 0.1

        else:
            taxRate = 0
        
        taxPayable = stocksMin.total * taxRate
        taxPayable = round(taxPayable, 2)
        postTax = stocksMin.total - taxPayable
        postTax = round(postTax, 2)
        if i == 0 or i == 4 or i == 9:
            print(f"At the end of year {str(i+1)}")
            print(f"Your investment will be worth:")
            print(f"£{postTax}")
            print(f"\nTotal fees paid in this period: £{round((yearlyFees * (i+1)), 2)}")
            print(f"\nTotal profit in this period: £{postTax - round((yearlyFees * (i+1)), 2)}")
            print(f"\nTotal tax due in this period: £{taxPayable}")

    print("\n#####################################\n")

def savingsPrint():
    print("--------------------------------------------------------")
    print("Personal Investment Quote for:")
    print(f"Name: {opening.name}")
    print(f"\nTelephone Number: {opening.phone}")
    print("--------------------------------------------------------")
    print(f"\nYou selected a savings plan.")
    savingsMin()
    savingsMax()

def stocksPrint():
    print("--------------------------------------------------------")
    print("Personal Investment Quote for:")
    print(f"Name: {opening.name}")
    print(f"\nTelephone Number: {opening.phone}")
    print("--------------------------------------------------------")
    print("\nYou chose a Managed Stock Investment plan")
    stocksMin()
    stocksMax()

opening()
options()