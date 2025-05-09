import datetime
from RecieptGenerator import *

startDate: None
endDate: None
accomodationName = ""

def GetDaysOfStay():
    return int(input("Select the number of days you wish to stay\n> "))

def SelectBookingDates(numDays):
    global startDate,endDate
    print("___________________________")
    tDelta = datetime.timedelta(numDays)
    day = int(input("Select the day you wish to stay with the format 01 - 30\n> "))
    month = int(input("Select the month number you wish to stay in the format 01 - 12\n> "))
    year = int(input("Select the year you wish to stay\n> "))
    startDate = datetime.date(year,month,day)
    endDate = startDate + tDelta 

def CalcuatePrice(length, price, cardCost, discountRate):
    global startDate, endDate, accomodationName
    VAT = 1.35
    SelectBookingDates(length)
    price  = price * length
    price = price * VAT
    if length > 14:
        price -= (price * 0.1)
        print("Discount applied")

    price += cardCost
    GenerateReciept(startDate,endDate,price,accomodationName)

def BookingStart():
    print("_________________________________________________________")
    print("Welcome to our online booking service. Please enter the number of one of the below:")
    choice = input("1) Create a new booking\n2) Quit\n")
    if choice != "1":
        print("choice not made")
        return
    
    SelectAccomidation()

def SelectAccomidation():
    global accomodationName
    print("____________________________________________")
    print("Please select your accommodation choice")
    print("1) Paradise Villa: £370 per day")
    print("2) Sunshine Hut: £280")
    print("3) Standard Cabin: £200 per day")
    print("4) Treehouse: £160 per day")
    print("5) Classic Tipi: £120 per day")
    choice = int(input())
    price = 0
    cardCost = 0
    discountRate = 5
    match choice:
        case 1: #Paraside Villa
            price = 350
            cardCost = 4
            discountRate = 10
            accomodationName = "Paradise Villa"

        case 2: #Sunshine Hut
            price = 200
            cardCost = 3.50
            discountRate = 10
            accomodationName = "Sunshine Hut"

        case 3: #Standard Cabin
            price = 180
            cardCost = 3
            accomodationName = "Standard Cabin"

        case 4: #Treehouse
            price = 160
            cardCost = 2.50
            accomodationName = "Treehouse"

        case 5: #Classic Tipi
            price = 120
            cardCost = 2
            accomodationName = "Classic Tipi"
            quit()

    days = GetDaysOfStay()
    CalcuatePrice(days,price,cardCost,discountRate)