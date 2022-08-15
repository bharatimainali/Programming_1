# copied the book from the oppgave 3 and past it here toLord of the Rings trilogy.
list_of_the_books = ['Farmer Giles of Ham', #0
                     'Lord of the Rings: The Fellowship of the Ring', #1
                     'Lord of the Rings: The Return of the King', #2
                     'Lord of the Rings: The Two Towers',
                     'The Adventures of Tom Bombadil',
                     'The Hobbit', 'The Silmarillion',
                     'Tree and Leaf',
                     'Unfinished Tales']

# made a empty list
new_book_list = []

# Using a for loop to add lord of the rings books to the empty list.
for book in list_of_the_books:
    if "Lord of the Rings" in book:
        new_book_list.append(book)

# printing normal for loop.
print("Normal for loop:")
for book in new_book_list:
    print(book)

# using for loop with index
print("\nFor loop with index:")
for book in range(len(new_book_list)):
    print(new_book_list[book])
