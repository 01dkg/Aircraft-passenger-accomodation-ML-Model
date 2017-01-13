import sys
import sqlite3
import pandas as pd

def read_booking(n):
    column_names = ['passenger_name, no_of_passenger']
    df = pd.read_csv('bookings.csv', header=None)
    passenger_name = df.loc[n,0]  #Setting Index to 1 as index starts from 0
    no_of_passenger = df.loc[n,1]
    print(passenger_name,no_of_passenger)
    return passenger_name,no_of_passenger
#read_booking(1)


def read_seat_config():
    conn = sqlite3.connect('airline_seating.db')
    cur = conn.cursor()
    row_data = cur.execute('''select * from rows_cols''')
    for row in row_data:
        nrows = row[0]
        seat_config = row[1]
    print(nrows, seat_config)
    return nrows,seat_config
read_seat_config()