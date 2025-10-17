def validate_posint(prompt): # validates that the user has inputted a positive integer.
    print(prompt)
    while True:
        var = input("> ")
        try:
            var = int(var)
        except:
            print("input must be an integer. try again.")
            continue
        if var <= 0:
            print("input must be positive. try again.")
        else:
            return var

print("<== QUESTION I ==>")

nums = []
q1_total = 0

num_nums = validate_posint("enter the number of numbers.")

for i in range(num_nums):
    num = validate_posint(f"enter number number {i + 1}.")
    nums.append(num)

for num in nums:
    q1_total += num

print(f"the total of all of these numbers is {q1_total}.")


print("\n\n<== QUESTION II ==>")

x = "5"
y = "39"
z = "100"

for val in [x, y, z]:
    val = int(val)
    print(val)


print("\n\n<== QUESTION III ==>")

def fib(len):
    seq = [0, 1]
    for i in range(2, len):
        val = seq[i - 1] + seq[i - 2]
        seq.append(val)
    return seq

seq_len = validate_posint("enter the length of the fibonacci sequence.")
q3_seq = fib(seq_len)
print(q3_seq)


print("\n\n<== QUESTION IV ==>")

for counter in range(1, 11):
    print("Current value:", counter)


print("\n\n<== QUESTION V ==>")

list = []
nineteens = 0
fives = 0

list_len = validate_posint("enter the length of the list.")

for i in range(list_len):
    num = validate_posint(f"enter number number {i + 1}")
    list.append(num)

for num in list:
    if num == 19:
        nineteens += 1
    if num == 5:
        fives += 1

if nineteens == 2 and fives >= 3:
    print("True")
else:
    print("False")


print("\n\n<== QUESTION V ==> (again, yes it says question 5 twice)")

with open("file.txt", "w") as file:
    file.write(f"QUESTION 1 OUTPUT: {q1_total}\nQUESTION 3 OUTPUT: {q3_seq}")
print("outputs of questions 1 and 3 written to file.txt.")