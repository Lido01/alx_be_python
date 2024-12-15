book_stack = ["Tesfu", "Dame", "Tesfa","Bisire","Lido","Betty"]
desired_book = input("Enter who you want to communicate with?")
book_found = False
while book_stack:
    current_book = book_stack.pop()
    if current_book == desired_book:
        print("you found the desired family memeber, right away!")
        book_found = True
        break
if not book_found:
    print("The desured family member is not found, try again.")