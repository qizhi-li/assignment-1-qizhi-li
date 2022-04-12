"""
Replace the contents of this module docstring with your own details
Name:QIZHLI
Date started:11/04/2022
GitHub URL:
"""

import csv


class Book():
    def __init__(self,star,number,name, author,page_count,finished_reading) :
        self.star=star
        self.name =name
        self.author = author
        self.page_count = page_count
        self.finished_reading = finished_reading
        self.number=number
    def __str__(self):
        complete = '*' if self.finished_reading == 'r' else ''
        return '"%s" "%s" "name: 《%s》 author: %s page: <%s> reading: %s' \
               % (self.number,complete,self.name, self.author, self.page_count,self.finished_reading)



class BookManage(object):
    books=[]
    def init(self):

        self.books.append(Book("","1","Developing the Leader Within You", 'John Maxwell', 225, "c"))
        self.books.append(Book("","2","The 360 Degree Leader", 'John Maxwell', 369,"r"))
        self.books.append(Book("","3","In Search of Lost Time", 'Marcel Proust', 93, "c"))
        self.books.append(Book("","4","The Practice of Computing Using Python", 'Punch and Enbody', 792, "r"))
        print("4 books loaded")


    def showAllBook(self):
      sum = 0
      numbers=0
      for book in self.books:
        print(book)
        if book.finished_reading=="r":
         sum+=book.page_count
         numbers+=1
      print("You need to read"+str(sum)+"pages""in"+str(numbers)+"books.")

      if book.finished_reading!="r":
          print("No books left to read. Why not add a new book?")

    def entering(self):
         while True:
           name = input("Tittle：").strip()
           if name !="":
              break
         else:
                print("Input can not be blank")

         while True:
            Author = input("Author：").strip()
            if Author != "":
               break
         else:
               print("Input can not be blank")
         while True:
             try:
                 pages = input('Pages: ')
                 pages= int(pages)
                 break
             except ValueError:
                 print("Invalid input; enter a valid number")

         numbers=4
         while True:
             numbers+=1
             break

         self.books.append(Book("",numbers,name, Author,pages,"r"))
         print(name,"by",Author,(pages),"added to Reading Tracker")

    def checkBook(self, number):
        for book in self.books:
            if int(book.number)==int(number) and book.finished_reading== "r":
             return book
        else:
            return None

    def Mark(self):

        sum = 0
        numbers = 0
        for book in self.books:
           print(book)
           if book.finished_reading== "r":
                sum += book.page_count
                numbers += 1

        print("You need to read" + str(sum) + "pages""in" + str(numbers) + "books.")
        print("Enter the number of a book to mark as completed")


        if book.finished_reading!="r":
            print("No required books")
        else:



         while True:

            try:
               number = input("Number：").strip()
               number = int(number)
               ret = self.checkBook(number)
               if number<0:
                  print("Number must be > 0")
               elif number>int(book.number):
                   print("Invalid book number")
               elif ret==None:
                   print("That book is already completed")
                   break
               elif ret!=None:
                   ret.finished_reading = 'c'
                   print(ret.name,"by",ret.author,"completed!")
                   break
            except ValueError:
             print("Invalid input; enter a valid number")
             return book
    def quit(self):

        filename = 'booksdata.csv'
        with open(filename, mode='w') as f:
            write = csv.writer(f, dialect='excel')
            write.writerow(self.books)
        print("6 books saved to books.csvSo many books, so little time. Frank Zappa")













def main():
    """..."""
    print("Reading Tracker 1.0 - QIZHILI")
    # 创建书籍管理的对象
    bm = BookManage()
    # 先初始化书籍信息
    bm.init()


    while True:
        print("""
        Menu:
        L -List all books
        A -Add new book
        M -Mark a book as completed
        Q -Quit


        chooce：""")
        choice = input().upper()
        if choice == 'L':
            bm.showAllBook()
        elif choice == 'A':
            bm.entering()
        elif choice == 'M':
            bm.Mark()

        elif choice == 'Q':
            bm.quit()
            break
        else:
            print("Invalid menu choice")


if __name__ == '__main__':
    main()
