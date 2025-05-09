with open("C:\\Users\\s2259223\\OneDrive - NCG\\code\\programming problem solving and esp\\actual code\\stuff_with_multiple_files\\collatz\\largest.txt") as file:
    content = file.readlines()
    largest = content[0]

c = int(largest)
proven = True
while proven:
    c0 = c
    list = []
    while c0 != 1:
        if c0 % 2 == 0:
            c0 /= 2

        else:
            c0 = (3 * c0) + 1

        list.append(c0)
        count = 0
        for num in list:
            if num == c0:
                count += 1
                if count >= 9999:
                    proven = False
                    print(f"{c}: disproven")
                    input("congratulations, you have successfully disproven the collatz conjecture!")

    print(f"{c}: proven")
    with open("C:\\Users\\s2259223\\OneDrive - NCG\\code\\programming problem solving and esp\\actual code\\stuff_with_multiple_files\\collatz\\largest.txt", "w") as file:
        file.write(str(c))
        file.close()

    c += 1