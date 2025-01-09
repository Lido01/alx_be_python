# Prompt user for the size of patter
n = int(input("enter the pattern size"))
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
    