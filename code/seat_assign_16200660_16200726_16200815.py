 ######################################################################################################################
#                                                                                                                     #
#                                         ARI Programming Assignment                                                  #
#             Author: Deepak K Gupta and Shruti Goyal
#                                                                                                                     #
#######################################################################################################################
import sys
import sqlite3
import pandas as pd
import numpy as np

 ######################################################################################################################
#                                                                                                                     #
#                                         Functions Reading Values from Files and DB                                  #
#                                                                                                                     #
#######################################################################################################################


def read_seat_config():
    conn = sqlite3.connect('airline_seating.db')
    cur = conn.cursor()
    row_data = cur.execute('''select * from rows_cols''')

    for row in row_data:
        nrows = row[0]
        seat_config = row[1]
        seat_col = len(seat_config)
    return nrows,seat_config,seat_col


def read_rows_in_booking():
    df = pd.read_csv('bookings.csv', header=None)
    return (len(df))

nrows, seat_config, seat_col = read_seat_config()
total_booking = read_rows_in_booking()


def read_booking(n):
    column_names = ['passenger_name, no_of_passenger']
    df = pd.read_csv('bookings.csv', header=None)
    passenger_name = df.loc[n,0]  #Setting Index to 1 as index starts from 0
    no_of_passenger = df.loc[n,1]
    return passenger_name,no_of_passenger

#Seat Matrix
#0 is empty, 1 is occupied
def generate_seat_map():
    nrows, seat_config, seat_col = read_seat_config()
    seats = np.zeros(shape=(nrows, seat_col))
    return seats

seats = generate_seat_map()

 ######################################################################################################################
#                                                                                                                     #
#                                         Validity Functions                                                          #
#                                                                                                                     #
#######################################################################################################################

'''
Function Name: check_overbooking()
Description: This function first find the total number of passengers from the booking list, if booking is more than
the number of available seats in a aircraft then program will exit(0). However, program should accept all passenger till
it is has no space to accommodate any new passenger.
'''


def check_overbooking():
    nrows, seat_config, seat_col = read_seat_config()
    passenger_total =0
    for i in range(nrows):
        passenger_name, no_of_passenger = read_booking(i)
        passenger_total +=no_of_passenger
    if passenger_total > (seat_col*nrows):
        print("Cannot Proceed: No. of Passenger can't be more than no. of available seats")
        exit(0)


def is_empty_booking_list():
    nrows, seat_config, seat_col = read_seat_config()
    for i in range(nrows):
        passenger_name, no_of_passenger = read_booking(1)
        if passenger_name == "" or no_of_passenger ==0 or no_of_passenger == " ":
            print("Cannot Proceed: Passenger Information is Missing")
            exit(0)

#######################################################################################################################
#                                                                                                                     #
#                                         Seat Tracker Functions                                                      #
#                                                                                                                     #
#######################################################################################################################


def create_seat_tracker():
     empty_seat_row =[]
     for i in range(nrows):
         empty_seat_row.append(seat_col)
     return empty_seat_row


def update_seat_tracker(empty_seat_row,row):
    val = empty_seat_row[row]
    empty_seat_row[row]=val-1
    return empty_seat_row

create_seat_tracker()

#######################################################################################################################
#                                                                                                                     #
#                                         Single Seat Allocation                                                      #
#                                                                                                                     #
#######################################################################################################################


def single_seat_allocation(passenger_name,no_of_passenger):
    for i in range(nrows):
        for j in range(seat_col):
           if seats[i][j] == 0.0:
               seats[i][j] = 1.0
               return i, j


#######################################################################################################################
#                                                                                                                     #
#                                         Case 2 Group Seats                                                          #
#                           no_of_passenger > 1 or no_of_passenger <= seat_col                                        #
#                                                                                                                     #
#######################################################################################################################
def group_seat_available_row(passenger_name,no_of_passenger):
    for i in range(nrows):
         if empty_seat_row[i] >= no_of_passenger:
            return i

def group_seat_check(passenger_name,no_of_passenger):
    row = group_seat_available_row(passenger_name,no_of_passenger)
    temp = []
    for j in range(seat_col):
        if seats[row][j] == 0:
            temp.append(j)
    return temp,row

def group_seat_allot(passenger_name,no_of_passenger):
    temp, row = group_seat_check(passenger_name,no_of_passenger)
    seat_allocated = []
    print(temp)
    for i in range(no_of_passenger):
        col = temp[i]
        seat_allocated.append(col)
        seats[row][col] = 1
        update_seat_tracker(empty_seat_row, row)
        print("Seat Allocated to ", passenger_name, " is [",row,col,"]")
    return seat_allocated,row

#######################################################################################################################
#                                                                                                                     #
#                                         Case 2 Group Seats                                                          #
#                                        no_of_passenger > seat_col                                                   #
#                                                                                                                     #
#######################################################################################################################
def group_seat_available_row2(no_of_passenger):
    for i in range(nrows-1):
         if empty_seat_row[i] + empty_seat_row[i+1] >= no_of_passenger:
            return i

def group_seat_check2(passenger_name, no_of_passenger):
    row = group_seat_available_row2(no_of_passenger)
    next_row = row+1
    print(seats[row],seats[next_row])

def group_seat_allot2(passenger_name,no_of_passenger):
    group_seat_check2(passenger_name, no_of_passenger)


#######################################################################################################################
#                                                                                                                     #
#                                         Main Function Call and Body                                                 #
#                                                                                                                     #
#######################################################################################################################

def _main_():
    for n in range(total_booking):
        passenger_name, no_of_passenger = read_booking(n)
        if no_of_passenger == 1:
            i,j = single_seat_allocation(passenger_name,no_of_passenger)
            '''
            Calling database here to update seat number
            '''
            print("Seat Allocated to ",passenger_name, " is >>",i,j)
            update_seat_tracker(empty_seat_row,i)
        elif no_of_passenger > 1 or no_of_passenger <= seat_col:
            group_seat_allot(passenger_name,no_of_passenger)
        else:
            group_seat_allot2(passenger_name, no_of_passenger)

empty_seat_row = create_seat_tracker()
_main_()
print(empty_seat_row)
print(seats)