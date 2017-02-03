import sys
import sqlite3
import pandas as pd


def read_seat_config():
    conn = sqlite3.connect('airline_seating.db')
    cur = conn.cursor()
    row_data = cur.execute('''select * from rows_cols''')
    for row in row_data:
        nrows = row[0]
        seat_config = row[1]
    return nrows,seat_config


def create_seat_map():
    nrows,seat_config = read_seat_config()
    seat_number = []
    seats = [{str(nrows)+ltr:'Empty' for ltr in seat_config} for seats in range(1,nrows+1)]
    for seat_col in range(1,nrows+1):
        for ltr in seat_config:
            seat_number.append(str(seat_col) + ltr)
    return seats, nrows, seat_config, seat_number

create_seat_map()


def read_booking(n):
    column_names = ['passenger_name, no_of_passenger']
    df = pd.read_csv('bookings.csv', header=None)
    passenger_name = df.loc[n,0]  #Setting Index to 1 as index starts from 0
    no_of_passenger = df.loc[n,1]
    return passenger_name,no_of_passenger


def allot_seats():
    for n in range(1,10):
        passenger_name, no_of_passenger = read_booking(n)
        if no_of_passenger == 1:
            single_seat_allocation(passenger_name,no_of_passenger)
        else:
            family_seat_allocation(passenger_name,no_of_passenger)

def single_seat_allocation(passenger_name,no_of_passenger):
    seats, nrows, seat_config, seat_number = create_seat_map()
    for i in range(1,nrows+1):
        for j in seat_number:
            seatsx = str(j)
            print(seats[i]['1A'])


def any_seat_allocation(passenger_name,no_of_passenger):
    print("Naeee")


def family_seat_allocation(passenger_name,no_of_passenger):
    print("Yayaya")
allot_seats()
