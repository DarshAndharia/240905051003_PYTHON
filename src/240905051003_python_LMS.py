class Book: 
    def __init__(self, book_id, title, author, quantity, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.price = price
        self.active = True

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
    
    def add_book(self):
        book_id = input("Enter Book ID: ")
        if any(book.book_id == book_id for book in self.books):
            print("Error: Book ID already exists!")
            return
        
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        
        self.books.append(Book(book_id, title, author, quantity, price))
        print("Book added successfully!\n")
    
    def display_all_books(self):
        active_books = [book for book in self.books if book.active]
        if not active_books:
            print("No active books available!\n")
            return
        
        print("\n1. Sort by Book ID\n2. Sort by Title\n")
        choice = input("Select sorting option: ")
        
        if choice == "1":
            active_books.sort(key=lambda x: x.book_id)
        elif choice == "2":
            active_books.sort(key=lambda x: x.title)
        
        print("\n" + "="*70)
        print(f"{'ID':<10} {'Title':<20} {'Author':<15} {'Qty':<5} {'Price':<10}")
        print("="*70)
        for book in active_books:
            print(f"{book.book_id:<10} {book.title:<20} {book.author:<15} {book.quantity:<5} ${book.price:<9.2f}")
        print("="*70 + "\n")
    
    def search_book(self):
        print("\n1. Search by Book ID\n2. Search by Title\n")
        choice = input("Select search option: ")
        
        if choice == "1":
            book_id = input("Enter Book ID: ")
            book = next((b for b in self.books if b.book_id == book_id and b.active), None)
        elif choice == "2":
            title = input("Enter Title: ")
            book = next((b for b in self.books if b.title.lower() == title.lower() and b.active), None)
        else:
            print("Invalid choice!\n")
            return
        
        if book:
            print(f"\nFound: {book.book_id} | {book.title} | {book.author} | Qty: {book.quantity} | Price: ${book.price}\n")
        else:
            print("Book not found!\n")
    
    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")
        book = next((b for b in self.books if b.book_id == book_id and b.active), None)
        
        if not book:
            print("Book not found!\n")
            return
        
        if book.quantity <= 0:
            print("Book not available!\n")
            return
        
        book.quantity -= 1
        print(f"Book issued successfully! Remaining quantity: {book.quantity}\n")
    
    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        book = next((b for b in self.books if b.book_id == book_id and b.active), None)
        
        if not book:
            print("Book not found!\n")
            return
        
        book.quantity += 1
        print(f"Book returned successfully! Updated quantity: {book.quantity}\n")
    
    def delete_book(self):
        print("\n1. Delete by Book ID\n2. Delete by Title\n")
        choice = input("Select delete option: ")
        
        if choice == "1":
            book_id = input("Enter Book ID: ")
            book = next((b for b in self.books if b.book_id == book_id and b.active), None)
        elif choice == "2":
            title = input("Enter Title: ")
            book = next((b for b in self.books if b.title.lower() == title.lower() and b.active), None)
        else:
            print("Invalid choice!\n")
            return
        
        if book:
            book.active = False
            print("Book deleted successfully!\n")
        else:
            print("Book not found!\n")
    
    def run(self):
        while True:
            print("===== LIBRARY MANAGEMENT SYSTEM =====")
            print("1. Add Book")
            print("2. Display All Books")
            print("3. Search Book")
            print("4. Issue Book")
            print("5. Return Book")
            print("6. Delete Book")
            print("7. Exit")
            print("=" * 37)
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.display_all_books()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.issue_book()
            elif choice == "5":
                self.return_book()
            elif choice == "6":
                self.delete_book()
            elif choice == "7":
                print("Thank you for using Library Management System!")
                break
            else:
                print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.run()