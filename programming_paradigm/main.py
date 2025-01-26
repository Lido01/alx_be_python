"""
# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
"""
# Library Management 
# main.py

from library_management import Book, Library

def main():
    #Lidetu's added
    print(f"Here is avialable choose:")
    print(f"1. Add book")
    print(f"2. View")
    print(f"3. Check_out")
    print(f"4. Return")
    print(f"5. Exit")
    # Chosoe part
    choose = int(input(f"Choose you deserve: "))
    if True:
        if choose in [1,2,3,4,5]:
            match choose:
                case 1:
                    library = Library()
                    title = input("enter the title: ")
                    author = input(f"enter the author:")                
                    library.add_book(Book(title, author))
                    print(f"you added {title} with {author} sucesssfuly")
                case 2:
                    #Intialize list list of avilable books
                    print(f"Available books after setup:")
                    library.list_available_books()
                case 3:
                    # Simulate checking out a book
                    title = input(f"enter the book title")
                    library.check_out_book(title)
                case 4:
                    # Simulate returning a book
                    title = input(f"enter the title")
                    library.return_book(title)
                case 5:
                    #Break the loop
                    print(f"you Breaked the choose")
        else:
            print(f"Invalid input, choose correct input")
            main()
            
             
         

    # Setup a small library
    # library = Library()
    # library.add_book(Book("Brave New World", "Aldous Huxley"))
    # library.add_book(Book("1984", "George Orwell"))
    # library.add_book(Book("01_sina", "Lidetu Tesfaye"))
if __name__ == "__main__":
    main()
