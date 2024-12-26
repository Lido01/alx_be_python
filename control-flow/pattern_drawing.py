# Prompt user for the size of pattern
n = int(input("Enter the size of the pattern:"))
for i in range(10):
    print(n, "*" ,i+1,"=",n*(i+1))
