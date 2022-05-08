This is a project on Student and Library Management System. In this project, the
user can find the details of a particular student and also find the details of a particular
book and issue or return it. To do all this, the user needs to have the access of the
database. Without the access, no one can use the database.

On running the program, it first asks the user to enter their ‘User ID’ and ‘Password’. If
the user enters wrong credentials, then the program terminates with a message
showing whether the User Id or the Password was incorrect.

On successful login, the user is given six options:

i. Search the data of a particular student

ii. See the list of all books available in library

iii. See the current status of a particular book

iv. Issue a particular book

v. Return a book

vi. Exit

If the user chooses a wrong option, then the program will again ask to choose a correct
option, until the user chooses the correct option. Then the program will run as per the
option selected. It will close only if the user selects the option to exit.

To search the data of student, the user first need to enter the URN of student and then
the program will access the database and will retrieve the table containing the data of
all the student and then search for the particular student. If the data is found then it will
return the details of the student, otherwise it will return “Student not found”.

To see the list of all the books, the program accesses the database and retrieve the
table containing all the books data and then will display it to the user.

To see the current status of a particular book, the user first need to enter the BOOK_ID
of book and then the program will access the database and will retrieve the table
containing the data of all books and then search for the particular book using the
book_id. If the data is found then it will return the current status of the book, otherwise
it will return “Book not found”.

To issue a book, the user first need to enter the BOOK_ID of the book. The program
will check whether the book is available or not. If it is not available it will return “Book
not available”, otherwise it will ask the user for its URN and if the user has no book
issued to him/her currently, then the program will add the Name, CRN, URN, BOOK_ID,
Issue_Date to the library table and decrease the count of the book by one. The condition
to issue book is that the book must be available in the library and the user must not
have any book issued to his/her name.

The same process is followed to return the book. The user enters its URN and the
program searches for it in the library table and if name is found then the name is
removed and the count of book is increased by one.
