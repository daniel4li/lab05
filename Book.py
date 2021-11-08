class Book:
    def __init__(self, title="", author="", year=None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        return "Title: " + self.title + ", Author: " + self.author + ", Year: " + str(self.year)

    def __gt__(self, other):
        if (self.author > other.author):
             return True
        if (self.year > other.year):
            return True
        if (self.title > other.title):
            return True
        return False



