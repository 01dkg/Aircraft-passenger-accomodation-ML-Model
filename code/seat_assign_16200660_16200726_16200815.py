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

nrows, seat_config, seat_col = read_seat_config()

def read_booking(n):
    column_names = ['passenger_name, no_of_passenger']
    df = pd.read_csv('bookings.csv', header=None)
    passenger_name = df.loc[n,0]  #Setting Index to 1 as index starts from 0
    no_of_passenger = df.loc[n,1]
    return passenger_name,no_of_passenger


def generate_seat_map():
    nrows, seat_config, seat_col = read_seat_config()
    seats = np.zeros(shape=(nrows-1, seat_col-1))
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
    for i in range(nrows+1):
        passenger_name, no_of_passenger = read_booking(i)
        passenger_total +=no_of_passenger
    if passenger_total > (seat_col*nrows):
        print("Cannot Proceed: No. of Passenger can't be more than no. of available seats")
        exit(0)


def empty_booking_list():
    nrows, seat_config, seat_col = read_seat_config()
    for i in range(nrows + 1):
        passenger_name, no_of_passenger = read_booking(1)
        if passenger_name == "" or no_of_passenger ==0 or no_of_passenger == " ":
            print("Cannot Proceed: Passenger Information is Missing")
            exit(0)
#######################################################################################################################
#                                                                                                                     #
#                                         Seat Allocation Functions                                                   #
#                                                                                                                     #
#######################################################################################################################


def allot_seats():
    empty_booking_list()
    for n in range(nrows+1):
        passenger_name, no_of_passenger = read_booking(n)
        if no_of_passenger == 1:
            i,j = single_seat_allocation(passenger_name,no_of_passenger)
            print("Seat Allocated to ",passenger_name, " is >>",i,j)
            break
        else:
            family_seat_allocation(passenger_name,no_of_passenger)

def single_seat_allocation(passenger_name,no_of_passenger):
    seats, nrows, seat_config, seat_col = generate_seat_map()
    for i in range(nrows-1):
        for j in range(seat_col-1):
           if seats[i][j] == 0.0:
               seats[i][j] = 1.0
               break;
        break
    print(seats)
    return i,j

def find_empty_seats(no_of_passenger):
    count =0
    for i in range(nrows-1):
        for j in range(seat_col-1):
            if seats[i][j] ==0:
                count +=1
        if count <= no_of_passenger:


def any_seat_allocation(passenger_name,no_of_passenger):
    print("Naeee")


def family_seat_allocation(passenger_name,no_of_passenger):
    print("Yayaya")
allot_seats()
