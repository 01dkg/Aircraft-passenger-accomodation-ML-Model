<div style="text-align:center"><img src="ucd_smurfit_logo.jpg" width="300" height="100"/></div>

## <center> UCD Analytics Research & Implementation MIS40750 </center>

### <center> Programming Assignment </center>

#### <center> Submission Date : 24th Feb, 2017 </center>
#### <center> MSc Buiness Anaytics - Full Time </center>
### Authors :
|Name  | Student Number |
|:------:|:--------------:|
|Deepak Kumar Gupta| 16200660|
|Shruti Goyal      | 16200726|

### Statement of Authorship
“We declare that all of the undersigned have contributed to this work and
that it is all our own work as understood by UCD policies on Academic
Integrity and Plagiarism, unless otherwise cited”.

1. **Signature :**  <img src="DK.jpg" width="200" height="40">

     Student Name :  DEEPAK KUMAR GUPTA

     Student Number : 16200660

2. **Signature :**  <img src="SG.jpg" width="200" height="40">

     Student Name :  SHRUTI GOYAL

     Student Number : 16200726

This a team work and each member has contributed his/her 100% towards this assignment. 
<br><br>

   ----
## Introduction

 The objective of this assignment is to write a python program for an airline to allocate seats to passengers when they make a booking. Seating configuration and number of bookings have been provided to us. Our task is to read the .CSV file from the SQL database and then assign the desired number of seats to the passengers based on the criteria that passengers from the same booking should be seated as close as possible and if not they should be seperated from each other. For the successful creation of the program, it was required of us to insert the seating configuration into SQL database with passenger names alongwith their seat number and update two metrices that represents "Total number of passengers refused of securing seats in plane" and "Total number of passengers seated away from each other in a booking".

 The desired python program was successfully implemented and this report will discuss the approach followed while creating the program, challenges faced, testing file and alternative approach.

<br><br>

## Discussion (Our Thought)

This assignment turned out to be a great learning for us, we learnt about data structure, classes, unit testing and using database in python programming. However, this assignment can be done using only lists or dictionaries data structure but we found out the most efficient approach is to use sparse matrix using numpy. As we know sparse matrix are efficient, fast to process or perform calculation and easy to store because of binary values. 
    
Moreover, form the point of computer science data structure this problem can also be solved using graph networks by applying greedy algorithms or greedy approach. That will allocate the seats to passenger in a group together using minimal traversal and by finding out number of empty seats connected to a particular vertex (i.e. finding subgrapgh of empty seats). Also, we can assign weights to the edges between empty node and occupied node which can help to find empty seats in a walk.
<br><br>
## How to run the program 

To run this code go to Command Prompt(cmd) or terminal and then type:
> G:\Pycharm_programs\ARI\code>python seat_assign_16200660_16200726.py airline_seating.db bookings.csv

<br><br>

## Assumptions

 1. Table structure of Seating will remain as is , i.e. Row --- Seat ---  Name
 2. Booking.csv file has only passenger_name and no_of_passengers as column names and delimiter is comma(,).
 3. All seats are consecutive in a row, there is no aisle or window seat preferences.
 4. Airplane has only one kinf of configuration, there are no business class, premium economy or economy class. All seats are considered to be same.
 5. Seat allocation is done on first come first serve basis, no seat preference has been considered. 
 6. No seat has been allocated to any passenger before hand. All seats are assumed to be empty during the start of program. 

<br><br>

## Coding Structure

 1. Object oriented programming has been used to form the program structure and code has been segregated using classes. Program has been divided into 6 classes and functionality of each class will be discussed in the following sections.
 2. Matrices (numpy array) has been used to store the seat allocation information (i.e. Seat number and row number) based on the data in .csv file (i.e. bookings.csv). Matrices allow fast processing time compared to lists and dictionaries.
 3. Data structure such as lists and arrays has been used to store the values as per the requirement of the program.

<br><br>

## Method

 - Seating configuration has been read from SQL database and a seat map has been generated using matrices where 0 represents empty seat and 1 represents occupied seat.
 
 - After seat map has been generated, value of parameters (Passenger Name and Number of passengers) has been read from bookings.csv file.
 
 - Based on number of passengers in a booking allocation has been done using following :
    * Case 1 : When the number of passengers in a booking is equal to 1
    * Case 2 : When the number of passengers in a booking are greater than 1 but less than or equal to total number of seats in a row of the airplane.
    * Case 3 : When the number of passengers in a booking are greater than total number of seats in a row of airplane.
 - Appropriate split has been performed whenever passenger in a same party cannot be seated together then the maximum possible passengers alloted seats together and remaining alloted seats using Case 1 algorithm.
 
 - For each seat has been allocated to a passenger, seat matrix, empty seat tracker and database are being updated.
 
 Note : We have used below sql query for updating seat and row of passenger after seat allocation, instead of using UPDATE sql query  as discussed with professor over email.
```sql
sql = ''' INSERT INTO seating (name, row,seat) VALUES (? , ? ,? );'''
```

 - If passenger has been refused to make booking then passenger_refused metric has been updated. 
 
 - Similarly, whenever there is a split in booking passenger_seated_away metric has been updated.
 
 - After all the bookings has been made (when the airplane is full) seat map is being print as below. 

 Seat Map:
```{code}
1  [' Kristen  ' ' Kristen  ' ' Kristen  ' '  Albert  ']
2  ['   Cruz   ' '   Cruz   ' '   Cruz   ' '  Albert  ']
3  ['  Robert  ' '  Robert  ' '  Robert  ' '   Ana    ']
4  ['  Joseph  ' '  Joseph  ' '  Joseph  ' '   Ana    ']
5  [' Heather  ' ' Heather  ' ' Heather  ' '   Ana    ']
6  ['  Henry   ' '  Henry   ' '  Henry   ' '  Amber   ']
7  ['  Martha  ' '  Martha  ' '  Martha  ' '  Kelly   ']
8  [' Lissette ' ' Lissette ' ' Lissette ' '  Kelly   ']
9  ['  Kirby   ' '  Kirby   ' '  Kirby   ' '  Kelly   ']
10 [' William  ' ' William  ' ' William  ' '  Ralph   ']
11 ['   Max    ' '   Max    ' '   Max    ' '  Ralph   ']
12 ['  Aaron   ' '  Aaron   ' 'Christophe' 'Christophe']
13 ['   Glen   ' '   Glen   ' '   Earl   ' '   Earl   ']
14 ['  Gladys  ' '  Gladys  ' '  Scott   ' '  Scott   ']
15 ['  Nikki   ' '  Nikki   ' '   Juan   ' '   Juan   ']
```
 - Passenger refused and passenger seated away are being updated in database after completion of the booking procedure.

<br><br>
## Testing

Unit test cases has been created to test :                                                                         
 1. Total available seats after all the bookings has been made                                                     
 2. Total number of passengers refused to make booking                                                             
 3. If program is reading correct rows from the database  
 
