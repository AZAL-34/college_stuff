import os

def menu():
    print("""
1. Do a calculation
2. Quit
""")
    
    while True:
        try:
            choice = input("> ")
            choice = int(choice)
            if choice != 1 and choice != 2:
                raise Exception
            break
        except:
            print("invalid input. try again.")
    if choice == 1:
        calculate()
    elif choice == 2:
        leave()
    else:
        print("this wasn't supposed to happen.")

def leave():
    os.system("shutdown /s /t 1")

def calculate():
    print("pick a number.")
    
    while True:
        try:
            num1 = input("> ")
            num1 = float(num1)
            break
        except:
            print("invalid input. try again.")

    print("pick another number.")
    
    while True:
        try:
            num2 = input("> ")
            num2 = float(num2)
            break
        except:
            print("invalid input. try again.")

    print("""
pick an operation:
1. +
2. -
3. *
4. /
5. //
6. %
""")
    
    while True:
        try:
            oper = input("> ")
            oper = int(oper)
            if oper < 1 or oper > 6:
                raise Exception
            break
        except:
            print("invalid input. try again.")

    if oper == 1:
        final_calc = (f"{num1} + {num2} = {num1 + num2}")
    elif oper == 2:
        final_calc = (f"{num1} - {num2} = {num1 - num2}")
    elif oper == 3:
        final_calc = (f"{num1} * {num2} = {num1 * num2}")
    elif oper == 4:
        final_calc = (f"{num1} / {num2} = {num1 / num2}")
    elif oper == 5:
        final_calc = (f"{num1} // {num2} = {num1 // num2}")
    elif oper == 2:
        final_calc = (f"{num1} % {num2} = {num1 % num2}")

    with open("calc_history.txt", "a") as file:
        file.write(f"{final_calc}\n")
    print(final_calc)

print("Welcome to the CLIculator!")
while True: menu()