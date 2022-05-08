CREATE DATABASE DBMS_PROJECT;
USE DBMS_PROJECT;
CREATE TABLE STUDENT_INFORMATION
(
	NAME VARCHAR(120) NOT NULL,
    BRANCH VARCHAR(10) NOT NULL,
    CRN INT NOT NULL,
    URN INT NOT NULL,
    PHONE_No VARCHAR(10),
    EMAIL VARCHAR(200),
    PRIMARY KEY (URN)
);
CREATE TABLE LIBRARY
(
    NAME VARCHAR(120) NOT NULL,
    CRN INT NOT NULL,
    URN INT NOT NULL,
    ISSUE_DATE DATE NOT NULL,
    BOOK_ID VARCHAR(20),
    FOREIGN KEY (URN) REFERENCES STUDENT_INFORMATION(URN),
	FOREIGN KEY (BOOK_ID) REFERENCES BOOKS(BOOK_ID)
);
CREATE TABLE BOOKS
(
	BOOK_NAME VARCHAR(100) NOT NULL,
    AUTHOR_NAME VARCHAR(120) NOT NULL,
    PUBLISHER_NAME VARCHAR(120) NOT NULL,
    TOTAL_BOOKS INT NOT NULL,
    BOOKS_REMAINING INT NOT NULL,
    BOOK_ID VARCHAR(20),
    PRIMARY KEY (BOOK_ID)
);
INSERT INTO STUDENT_INFORMATION
VALUES
( 'Abhinav Saini', 'CSE', '1915003', '1904972', '7814980141','abhinav1915003@gndec.ac.in'),
( 'Abhishek Kumar', 'CSE', '1915004', '1904974', '8521343374', 'abhishek1915004@gndec.ac.in'),
( 'Abhishek Tiwari', 'CSE', '1915005','1904975','6283409546', 'abhishek1915005@gndec.ac.in'),
( 'Aman Malhotra', 'CSE', '1915006', '1904976',	'6284085887', 'aman1915006@gndec.ac.in'),
( 'Anshik Thakur', 'CSE', '1915009', '1904979', '7973990693', 'anshik1915009@gndec.ac.in'),
( 'Anurag Pandey', 'CSE', '1915010', '1904980', '9810541660', 'anurag1915010@gndec.ac.in'),
( 'Ashutosh Dhingra', 'CSE', '1915013', '1904981', '9915035586', 'ashutosh1915013@gndec.ac.in'),
( 'Ashwin Mohan', 'CSE', '1915014', '1904982', '8847218892', 'ashwin1915014@gndec.ac.in'),
( 'Bhavneet Singh', 'CSE', '1915015', '1904983', '8427447113', 'bhavneet1915015@gndec.ac.in'),
( 'Chetan Gupta', 'CSE', '1915017',' 1904985', '9914182634', 'chetan1915017@gndec.ac.in'),
( 'Chirag Sabharwal', 'CSE', '1915018', '1904986', '7009958566', 'chirag1915018@gndec.ac.in'),
( 'Ekamjot Singh', 'CSE', '1915020', '1904988', '9877308806', 'ekamjot1915020@gndec.ac.in'),
( 'Gurashish Singh', 'CSE', '1915022', '1904990', '8360440332', 'gurashish1915022@gndec.ac.in'),
( 'Gurdeep Singh', 'CSE', '1915023', '1904991', '9855507091', 'gurdeep1915023@gndec.ac.in'),
( 'Gurinder Singh', 'CSE', '1915024', '1904992', '946580783', 'gurinder1915024@gndec.ac.in'),
( 'Gurjot Singh', 'CSE', '1915025', '1904993', '9501863306', 'gurjot1915025@gndec.ac.in'),
( 'Harkirat Singh', 'CSE', '1915031', '1904999', '6239572909', 'harkirat1915031@gndec.ac.in'),
( 'Harpreet Singh', 'CSE', '1915032', '1905000', '7888603235', 'harpreet1915032@gndec.ac.in');
SET SQL_SAFE_UPDATES = 0;
INSERT INTO BOOKS
VALUES
( 'Artificial Intelligence', 'Elaine Rich and Kevin Knight', 'Tata McGraw Hill', '25', '25', 'AI101'),
( 'An Approach to Artificial Intelligence', 'Trivedi', 'Khanna Publishing House', '20', '20', 'AI102'),
( 'Artificial Intelligence: Foundations for Computational Agents', 'David Poole and Alan Mackworth', 'Cambridge University', '20', '20', 'AI103'),
( 'Database System Concepts', 'Abraham Silberschatz, Henry F, Korth, S. Sudarshan', 'McGraw Hill Education', '25', '25', 'DBMS101'),
( 'Fundamentals of Database Systems', 'RamezElmasri, Shamkant B Navathe', 'Pearson Education', '25', '25', 'DBMS102'),
( 'Database Management Systems', 'Alexis Leon, Mathews Leon', 'Database Management Systems', '20', '20', 'DBMS103'),
( 'Introduction to Automata Theory, Languages and Computation', 'John E. Hopcroft, Rajeev Motwani, Jeffrey D. Ullman', 'Pearson Education',  '20', '20', 'FLAT101'),
( 'Theory of Computer Science', 'K.L.P. Mishra and N. Chandrasekaran', 'PHI Learning Private Limited', '25', '25', 'FLAT102'),
( 'Formal Languages and Automata Theory', 'K.V.N. Sunitha, N. Kalyani', 'McGraw-Hill', '30', '30', 'FLAT103'),
( 'Fundamentals of Computer Algorithms', 'Ellis Horowitz, Sartaj Sahni and S. Rajasekharan', 'Universities Press', '30', '30', 'DAA101'),
( 'Design and Analysis of Algorithms', 'P. H. Dave, H. B. Dave', 'Pearson Education', '25', '25', 'DAA102');