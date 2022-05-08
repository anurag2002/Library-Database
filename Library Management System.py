import mysql.connector
from datetime import date
adminList = [1904979, 1904980]              ##username and password of the admins who can access the data
passwordList = [12312300]
class DBAccess:                                 ##Making a Class DBAccess to Access the database
    def studentInfo(self, rollNo):              ##Function to give the information of the students whose rollno is given
        sql="SELECT * FROM STUDENT_INFORMATION"         ##Selecting all the Student data
        con=mysql.connector.connect(user="root",password="9810541660",host="127.0.0.1",database="DBMS_PROJECT")
        cursor = con.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()                  ##fetching all the students data and giving it to rows
        findURN = rollNo
        for row in rows:
            if(findURN in row):                 ##searching for the roll no in the list of student data
                print("The data of student you are searching is: ")
                print("Name: ", row[0])
                print("Branch: ", row[1])
                print("CRN: ", row[2])
                print("URN: ", row[3])
                print("Phone No: ", row[4])
                print("Email ID: ", row[5])                      ##printing and returning the data of the student
                print("\n########################################################################################################\n")
                return row
        print("Student data not found")         ##will be printed if the student data is not found
        print("\n########################################################################################################\n")
    def bookInfo(self):
        sql = "SELECT * FROM BOOKS"             ##Selecting all Books
        con = mysql.connector.connect(user = "root", password = "9810541660", host = "127.0.0.1", database = "DBMS_PROJECT")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("The list of all available books is: ")
        print(*rows, sep="\n")                  ##printing the list of all books
        print("\n########################################################################################################\n")
    def bookStatus(self,findBook):                       ##Function to find the status of the book
        sql = "SELECT * FROM BOOKS"
        con = mysql.connector.connect(user = "root", password = "9810541660", host = "127.0.0.1", database = "DBMS_PROJECT")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            if(findBook in row):
                print("\nThe status of Book you are searching is: ")      
                print("Book ID: ", row[5])
                print("Book Name: ", row[0])
                print("Author Name: ", row[1])
                print("Publisher Name: ", row[2])
                print("Books Remaining: ", row[4])                      ##printing and returning the current status of the book
                print("\n########################################################################################################\n")
                return row
        print("Book data not found")                   ##printing if book is not found
        print("\n########################################################################################################\n")
    def bookIssue(self):                        ##Function to issue a book
        bookID = input("Enter the Book ID of Book to issue: ")
        row = self.bookStatus(bookID)                 ##Getting the current status of the book
        bookCount = row[4]                      ##No of books remaining in library
        if(bookCount > 0):
            rollNo = int(input("Enter your university roll No: "))      ##Roll No of student
            rows = self.library()
            rollNoList = []                     ##List of roll no of students who have not returned the books
            for r in rows:
                rollNoList.append(r[2])
            if(rollNo not in rollNoList):       ##Checking if the student has returned all the books or not
                self.libIssue(bookID, rollNo)
                count = -1
                self.bookUpdate(bookID, count, bookCount)
                print("Book Issued")
                print("\n########################################################################################################\n")
            else:
                print("Clear dues first")
                print("\n########################################################################################################\n")
        else:
            print("Book not available")
            print("\n########################################################################################################\n")
    def bookReturn(self):                       ##Function to return the book
        rollNo = int(input("Enter your university roll No: "))          ##Roll No the student
        rows = self.library()
        if (bool(rows)):
            rollNoList = []
            for r in rows:
                rollNoList.append(r[2])              ##List of roll no of students who have not returned the books
            i = rollNoList.index(rollNo)
            bookID = rows[i][4]
            row = self.bookStatus(bookID)                 ##Getting the status of the book
            bookCount = row[4]                      ##No of books remaining
            if(rollNo in rollNoList):               ##Checking if the student has to return any book or not
                self.libReturn(rollNo)
                count = 1
                self.bookUpdate(bookID, count, bookCount)
                print("Book Returned")
                print("\n########################################################################################################\n")
            else:
                print("No Book to return")    
                print("\n########################################################################################################\n")
        else:
            print("No Book to return")    
            print("\n########################################################################################################\n")
    def bookUpdate(self, bookID, count, bookCount):         ##Function to update the books table
        sql="UPDATE BOOKS SET BOOKS_REMAINING = %s WHERE BOOK_ID = %s"      ##Updating the books table
        val = (bookCount + count, bookID)
        con=mysql.connector.connect(user="root",password="9810541660",host="127.0.0.1",database="DBMS_PROJECT")
        cursor=con.cursor()
        cursor.execute(sql, val)
        con.commit()
    def library(self):          ##Function to return the list of students who have borrowed the books
        sql = "SELECT * FROM LIBRARY"
        con = mysql.connector.connect(user = "root", password = "9810541660", host = "127.0.0.1", database = "DBMS_PROJECT")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows             ##Returning the list of students who have not returned books
    def libIssue(self, bookID, rollNo):         ##Function to Issue book and add it to records
        rows = self.studentInfo(rollNo)         ##Retrieving the data of students
        sql="INSERT INTO LIBRARY VALUE('{}','{}','{}','{}', '{}')".format(rows[0], rows[2], rows[3], date.today(), bookID)        ##Added the data to records
        con=mysql.connector.connect(user="root",password="9810541660",host="127.0.0.1",database="DBMS_PROJECT")
        cursor=con.cursor()
        cursor.execute(sql)
        con.commit()
    def libReturn(self, rollNo):                ##Function to Return the book and remove it from records
        sql="DELETE FROM LIBRARY WHERE URN = ('{}')".format(rollNo)         ##Removed the data from records
        con=mysql.connector.connect(user="root",password="9810541660",host="127.0.0.1",database="DBMS_PROJECT")
        cursor=con.cursor()
        cursor.execute(sql)
        con.commit()
def login(userID, password):                ##Function to login to the database
    if (userID not in adminList):
        if(password not in passwordList):           ##Checking if the credentials entered are correct or not
            print("User does not has access to the data")
            print("\n********************************************************************************************************\n")
            exit()
        else:
            print("UserID is Incorrect \nTry again later")
            print("\n********************************************************************************************************\n")
            exit()
    else:
        print("Welcome ")
        print("\n********************************************************************************************************\n")
        choice = 0
        while(choice != 6):                    ##Running the loop until user doesn't exit
            print("Select the operation you want to perform: ")         ##Showing the list of information
            print("1. Display Student's Information")
            print("2. Display Books List")
            print("3. Display the Status of a particular book")
            print("4. Issue a book")
            print("5. Return a book")
            print("6. To exit")
            choice = int(input("Enter your choice:  "))                 ##Entering the choice from the user
            print("\n########################################################################################################\n")
            db = DBAccess()                             ##Accessing the class
            if(choice == 1):                            ##checking the choices entered
                findURN = int(input("Enter the university roll No of student to find: "))          ##Taking the rollno of student to find
                db.studentInfo(findURN)
            elif(choice == 2):
                db.bookInfo()
            elif(choice == 3):
                findBook = input("Enter the Book ID of Book to find: ")         ##entering the ID of the book to find
                db.bookStatus(findBook)
            elif(choice == 4):
                db.bookIssue()
            elif(choice == 5):
                db.bookReturn()
            elif(choice == 6):
                print("Thank You")
                print("Exiting")
                print("\n********************************************************************************************************\n")
                exit()
            else:
                print("Wrong Input")
                print("Try Again")
                print("\n########################################################################################################\n")
            choice = 0
userID = int(input("Enter your User ID: "))                  ##Asking the userID and password
password = int(input("Enter your passoword: "))
print("\n********************************************************************************************************\n")
login(userID, password)                         ##Login to the database
