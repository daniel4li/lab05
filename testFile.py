from BookCollection import BookCollection
from Book import Book
from BookCollectionNode import BookCollectionNode


def test_book():
   b = Book("Ready Player One", "Cline, Ernest", 2011)
   assert b.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011" 
   assert ("Cline, Ernest" > "King, Stephen") == True