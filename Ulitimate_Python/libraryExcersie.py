# class Library:
#     def __init__(self):
#         self.books = 0
#         self.booksName = []
#         self.loadBooks()  # File se books load karne ke liye

#     def addBooks(self, n):
#         self.book = n
#         self.booksName.append(self.book)
        
#         # Book ko file me store karna
#         with open("books.txt", 'a') as file:
#             file.write(self.book + "\n")

#         self.books += 1
#         print(f'Book "{self.book}" added successfully!')

#     def loadBooks(self):
#         """File se books load karne ke liye"""
#         try:
#             with open("books.txt", 'r') as file:
#                 self.booksName = [line.strip() for line in file.readlines()]
#                 self.books = len(self.booksName)
#         except FileNotFoundError:
#             # Agar file nahi mili to koi masla nahi
#             self.booksName = []
#             self.books = 0

#     def showBooks(self):
#         if self.books == 0:
#             print("No books available.")
#         else:
#             print("\nBooks in Library:")
#             for book in self.booksName:
#                 print(f"- {book}")
#             print(f"\nTotal number of books: {self.books}")

# # Library object
# c1 = Library()

# # Add book
# c1.addBooks("adfs")

# # Show books
# c1.showBooks()






