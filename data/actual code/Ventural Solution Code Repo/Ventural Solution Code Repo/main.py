from LoginSystem import *
from BookingCreator import *
from sdfvadfvadfvdafvd import *

print("Welcome to Ventural Bookings\nAre you a user or admin?")
choice = input()
if choice == "admin":
    if AttemptLogIn() == False:
        AttemptLogIn()
        ReadFileBookings()

    elif AttemptLogIn() == True:
        ReadFileBookings()

elif choice == "user":
    BookingStart()

else:
    print("Invalid choice detected")