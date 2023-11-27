n = 5 # Кількість рядків

for i in range (1,n + 1):
    num = n
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end = " ")
        else:
            print(num, end = " ")
            num -= 1
    print(" ")

for i in range (1, n + 1):
    print("    ", end = "    ")
    num = 1
    for j in range (n, 0, -1):
        if j > i:
            print("", end = "")
        else:
            print(num, end = " ")
            num += 1
    print(" ")