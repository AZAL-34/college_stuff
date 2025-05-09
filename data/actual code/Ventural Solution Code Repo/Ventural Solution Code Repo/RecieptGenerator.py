def GenerateReciept(startDate, endDate,price,accomodationName):
  file = open("Bookings.txt","a")
  custName = input("Please insert your name:\n")
  custNumber = input("Please inesrt your phone number:\n")
  
  print("Creating receipt.....................")
  print(startDate.strftime('%d %B %Y'),"-",endDate.strftime('%d %B %Y'))
  print("£" + str(price))
  print(custName)
  print(custNumber)

  startDate = str(startDate.strftime('%d %B %Y'))
  endDate = str(endDate.strftime('%d %B %Y'))
  bookingDate = endDate + " - " + startDate + "\n"

  file.write(accomodationName + "\n")
  file.write(bookingDate)
  file.write("Price: "+ "£"+str(price) + "\n")
  file.write("__________________________________________"+ "\n")
  file.close()