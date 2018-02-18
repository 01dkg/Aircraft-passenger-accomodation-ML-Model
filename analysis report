## <center>Airline Seating Allocation using Machine learning model to avoid any overbooking, allocating preference seats to passenger and etc </center>

### <center> Programming Assignment </center>

#### <center> Submission Date : 24th Feb, 2017 </center>
#### <center> MSc Buiness Anaytics - Full Time </center>
### Authors :
|Name              | Student Number |
|:----------------:|:--------------:|
|Deepak Kumar Gupta| 16200660       |
|Shruti Goyal      | 16200726       |

### Statement of Authorship
“We declare that all of the undersigned have contributed to this work and
that it is all our own work as understood by UCD policies on Academic
Integrity and Plagiarism, unless otherwise cited”.

This is a team work and each member has contributed his/her 100% towards this assignment.

**Contribution :**

|Name              | Contribution |
|:----------------:|:--------------:|
|Deepak Kumar Gupta| Algorithm Design, Coding, Testing, Documentation       |
|Shruti Goyal      | Algorithm Design, Coding, Testing, Documentation       |

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
```commandline
G:\Pycharm_programs\ARI\code>python seat_assign_16200660_16200726.py airline_seating.db bookings.csv
```
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
 ##### Before Seat Allocation, Seat Map in matrix form :
 ```commandline
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
```
 ##### After Seat Allocation, Seat Map in matrix form :
 ```commandline
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]
```

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

```python
if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Acceting booking csv file name as second system argument
        db = sys.argv[1]
        filename = sys.argv[2]
        __main__(db,filename)                                                                   

        print("-------------------Testing Data-------------------")
        suite = unittest.TestSuite()
        suite.addTest(test_after_total_seats("test_total_available_seats",db,filename))
        suite.addTest(test_after_total_seats("test_passenger_refused",db,filename))
        suite.addTest(test_after_total_seats("test_passenger_refused2", 'test.db','test_bookings.csv'))
        suite.addTest(test_after_total_seats("test_read_seat_config", db, filename))
        unittest.TextTestRunner().run(suite)
    else:
        print("Enter valid *.db and *.csv filenames.")
```                                                   

To carry out unit testing of functions in this program we have used TestSuite() method of unittest package in python. By using TestSuite() method we can add multiple test case scenario to a Test Suite using addTest() method, this helps in carrying out unit testing thoroughly and rigorously. And this is excellent way of debugging the program.

Unit test cases has been created to test :                                                                         
 1. Total available seats after all the bookings has been made : Expected result is 0 and actual value is 0 then test case will pass else fail.  
 ```python
    def test_total_available_seats(self):                      
        seats_available = total_available_seats(empty_seat_row)
        self.assertEqual(seats_available,0)
```
 2. Total number of passengers refused to make booking : Expected value is 180 and actual value is 180 then test case will pass else fail.
```python
    def test_passenger_refused(self):
        passenger_seated_away ,passenger_refused= __main__(self.db,self.filename)
        self.assertEqual(passenger_refused,180)
```                                                              
 3. If program is reading correct rows from the database : Expected value is 15 and actual value is 15 then test case will pass else fail.
    
    nrows = number of rows read from rows_col
```python
    def test_read_seat_config(self):
        nrows, seat_config, seat_col = read_seat_config()
        self.assertEqual(nrows,15,msg="Reading Correct Rows")
```

## Output

#####Program output for test.db and bookings1.csv file (Files are available on github).

```commandline
G:\Pycharm_programs\ARI\code>python seat_assign_16200660_16200726.py test.db bookings1.csv
Kristen Frost seat -> 1A
Cruz Hayes seat -> 1C
Robert Brailey seat -> 2A
Robert Brailey seat -> 2C
Robert Brailey seat -> 2D
Joseph Bean seat -> 1D
Passenger Refused So Far 0.0
Passenger Seated Away 0
-----------------------Seat Map of Fully Booked Plan is -----------------------
1 [' Kristen  ' '   Cruz   ' '  Joseph  ']
2 ['  Robert  ' '  Robert  ' '  Robert  ']
Unicode Error: try to run from python environment
Unicode Error: try to run from python environment
[[ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]]
-------------------Testing Data-------------------
FKristen Frost seat -> 3A
Cruz Hayes seat -> 3C
Robert Brailey seat -> 4A
Robert Brailey seat -> 4C
Robert Brailey seat -> 4D
Joseph Bean seat -> 3D
Passenger Refused So Far 0.0
Passenger Seated Away 0
-----------------------Seat Map of Fully Booked Plan is -----------------------
1 [' Kristen  ' '   Cruz   ' '  Joseph  ']
2 ['  Robert  ' '  Robert  ' '  Robert  ']
3 [' Kristen  ' '   Cruz   ' '  Joseph  ']
4 ['  Robert  ' '  Robert  ' '  Robert  ']
[[ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]]
FFlight is Fully Booked  Kristen Frost
Flight is Fully Booked  Cruz Hayes
Flight is Fully Booked  Robert Brailey
Flight is Fully Booked  Joseph Bean
Passenger Refused So Far 6.0
Passenger Seated Away 0
-----------------------Seat Map of Fully Booked Plan is -----------------------
1 [' Kristen  ' '   Cruz   ' '  Joseph  ']
2 ['  Robert  ' '  Robert  ' '  Robert  ']
3 [' Kristen  ' '   Cruz   ' '  Joseph  ']
4 ['  Robert  ' '  Robert  ' '  Robert  ']
[[ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]]
FF
======================================================================
FAIL: test_total_available_seats (__main__.test_after_total_seats)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "seat_assign_16200660_16200726.py", line 527, in test_total_available_seats
    self.assertEqual(seats_available,0)
AssertionError: 6 != 0

======================================================================
FAIL: test_passenger_refused (__main__.test_after_total_seats)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "seat_assign_16200660_16200726.py", line 531, in test_passenger_refused
    self.assertEqual(passenger_refused,216)
AssertionError: 0.0 != 216

======================================================================
FAIL: test_passenger_refused2 (__main__.test_after_total_seats)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "seat_assign_16200660_16200726.py", line 535, in test_passenger_refused2
    self.assertEqual(passenger_refused,120)
AssertionError: 6.0 != 120

======================================================================
FAIL: test_read_seat_config (__main__.test_after_total_seats)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "seat_assign_16200660_16200726.py", line 539, in test_read_seat_config
    self.assertEqual(nrows,15,msg="Reading Correct Rows")
AssertionError: 4 != 15 : Reading Correct Rows

----------------------------------------------------------------------
Ran 4 tests in 1.262s

FAILED (failures=4)

```
