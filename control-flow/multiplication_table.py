number = int(input("Enter a number to see its multiplication table:"))
for number in range(number-1, number):
    for j in (1, 10):
        print(number, "*", j, " = ",number * j)