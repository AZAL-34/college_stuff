def AttemptLogIn():
    logins = {}
    with open("adminLogins.txt") as file:
        for line in file:
            (key, val) = line.split()
            logins[(key)] = val

    print("Login to your admin account:")
    userName = input("Username: ")
    passWord = input("Password: ")
    nameExists = logins.__contains__(userName)

    if nameExists == True:
        return True
    
    if passWord == logins.get(userName):
        return True
    
    return False
    
def ReadFileBookings():
  print("_______________________________________")
  file = open("Bookings.txt", "r")
  print(file.read())