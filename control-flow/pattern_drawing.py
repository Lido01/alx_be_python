# Prompt user for the size of pattern
n = int(input("Enter the size of the pattern:"))
for i in range(1, 11):
    print(n, "*" ,i,"=",n*i)
