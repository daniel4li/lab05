from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection():
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def getNumberOfBooks(self):
        return self.size
    def insertBook(self,book):
        cur = self.head
        pre = None
        stop = False
        while cur != None and not stop:
            if cur.getData()> book:
                stop = True
            else:
                pre = cur
                cur = cur.getNext()
        temp = BookCollectionNode(book)
        if pre == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(cur)
            pre.setNext(temp)
        self.size += 1
    
            
    def getAllBooksInCollection(self):
        cur = self.head
        ans = []
        while cur is not None:
            ans.append(cur.data.getBookDetails())
            cur = cur.next
        return "\n".join(ans) 

    def getBooksByAuthor(self, author):
        cur = self.head
        ans = []
        while cur is not None:
            if cur.data.author == author:
                ans.append(cur.data.author)
            cur = cur.next
        return "\n".join(ans) 

