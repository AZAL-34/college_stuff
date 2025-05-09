import random, time, sys, os, ctypes
number = random.randint(1,100)

name = input("What is your name?\n> ")
print(f"Welcome to the guessing game, {name}! I have chosen an integer from 1 to 20, and you have 4 chances to guess right. The consequences if you guess wrong are fatal.")
print("")
guess1 = int(input("What is your first guess? > "))
while True:
    if guess1 <= 100 and guess1 >= 1:
        break
    else:
        print("Sorry, that is not a valid answer. Please pick a number from 1 to 20.")
        guess1 = int(input("What is your first guess? > "))
        continue
print("")
if guess1 == number:
    print(f"Wow, first try! The number was {number}.")
    time.sleep(2)
    sys.exit()
elif guess1 > number:
    print(f"Sorry, that answer was too high. Don't worry {name}, you still have 3 tries left!")
else:
    print(f"Sorry, that answer was too low. Don't worry {name}, you still have 3 tries left!")
print("")
guess2 = int(input(f"What is your second guess? (Previous Guess: {guess1}) > "))
while True:
    if guess2 <= 100 and guess2 >= 1:
        break
    else:
        print("Sorry, that is not a valid answer. Please pick a number from 1 to 20.")
        guess2 = int(input(f"What is your second guess? (Previous Guess: {guess1}) > "))
        continue
print("")
if guess2 == number:
    print(f"Correct! The number was {number}.")
    print(f"Your guesses: {guess1} and {guess2}")
    time.sleep(2)
    sys.exit()
elif guess2 > number:
    print(f"Sorry, that answer was too high. Be careful {name}, you only have 2 tries left!")
else:
    print(f"Sorry, that answer was too low. Be careful {name}, you only have 2 tries left!")
print("")
guess3 = int(input(f"What is your third guess? (Previous Guesses: {guess1} and {guess2}) > "))
while True:
    if guess3 <= 100 and guess3 >= 1:
        break
    else:
        print("Sorry, that is not a valid answer. Please pick a number from 1 to 20.")
        guess3 = int(input(f"What is your third guess? (Previous Guesses: {guess1} and {guess2}) > "))
        continue
print("")
if guess3 == number:
    print(f"Third times the charm! The number was {number}.")
    print(f"Your guesses: {guess1}, {guess2} and {guess3}")
    time.sleep(2)
    sys.exit()
elif guess3 > number:
    print(f"Sorry, that answer was too high. Last try, {name}.")
else:
    print(f"Sorry, that answer was too low. Last try, {name}.")
print("")
guess4 = int(input(f"What is your final guess? (Previous Guesses: {guess1}, {guess2} and {guess3}) > "))
while True:
    if guess4 <= 100 and guess4 >= 1:
        break
    else:
        print("Sorry, that is not a valid answer. Please pick a number from 1 to 20.")
        guess3 = int(input(f"What is your final guess? (Previous Guesses: {guess1}, {guess2} and {guess3}) > "))
        continue
print("")
if guess4 == number:
    print(f"On the last try! The number was {number}.")
    print(f"Your guesses: {guess1}, {guess2}, {guess3} and {guess4}")
    time.sleep(2)
    sys.exit()
else:
    print(f"The answer was {number}. Goodbye, {name}.")
    time.sleep(2)
    ctypes.windll.kernel32.SetConsoleTitleW("Administrator: Command Prompt")
    time.sleep(2)
    print("")
    print("C:\Windows\System32>rmdir")
    time.sleep(1)
    ctypes.windll.kernel32.SetConsoleTitleW("Administrator: Command Prompt - rmdir")
    print("Deleting C:\Windows\System32...")
    os.system('shutdown -s')
    time.sleep(28)
    print("")
    print("Done.")
    time.sleep(2)
    sys.exit()