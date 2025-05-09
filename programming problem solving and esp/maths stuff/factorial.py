def factorial(num):
    try:
        num = int(num)
        fact = 1
        for x in range(num):
            fact *= x + 1
        return fact
    except ValueError:
        return "error"

print("give me a number.")
num = input("> ")
while not num.isdigit():
    print("a positive integer would be preferred.")
    num = input("> ")
num = int(num)
fact = factorial(num)
print(f"{num} factorial is {fact}.")