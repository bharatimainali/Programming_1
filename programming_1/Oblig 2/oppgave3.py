# I have writen all the books name given in oppgave 3.
list_of_the_books = ["The Hobbit",
                     "Farmer Giles of Ham",
                     "The Fellowship of the Ring",
                     "The Two Towers",
                     "The Return of the King",
                     "The Adventures of Tom Bombadil",
                     "Tree and Leaf"]
# Printing first two and last two books
print(list_of_the_books[0])
print(list_of_the_books[1])
print(list_of_the_books[len(list_of_the_books)-2])
print(list_of_the_books[len(list_of_the_books)-1])

# adding two books.
list_of_the_books.extend(["The Silmarillion", "Unfinished Tales"])

# Adding lord of the rings book prefix
list_of_the_books[list_of_the_books.index("The Fellowship of the Ring")] = "Lord of the Rings: " + list_of_the_books[list_of_the_books.index("The Fellowship of the Ring")]
list_of_the_books[list_of_the_books.index("The Two Towers")] = "Lord of the Rings: " + list_of_the_books[list_of_the_books.index("The Two Towers")]
list_of_the_books[list_of_the_books.index("The Return of the King")] = "Lord of the Rings: " + list_of_the_books[list_of_the_books.index("The Return of the King")]
print(list_of_the_books)

# sort the list out.
list_of_the_books.sort()
print(f"\nsorted list: {list_of_the_books}")
