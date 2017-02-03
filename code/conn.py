import sqlite3
conn = sqlite3.connect('airline_seating.db')
conn.execute('''drop table metrics''')
conn.execute('''drop table rows_cols''')
conn.execute('''drop table seating''')
print("Database Successfully Created")

''' Creating Metric Table'''
conn.execute('''CREATE TABLE metrics (passengers_refused int, passengers_separated int)''')

''' Creating Metric Table'''
conn.execute('''CREATE TABLE rows_cols (nrows int, seats varchar(16))''')

''' Creating Seating Table'''
conn.execute('''CREATE TABLE seating ( row int not null, seat char(1) not null, name varchar(255), constraint prim_key primary key (row, seat) )''')

''' Inserting Values in Tables'''

conn.execute('''insert into rows_cols values (15, 'ACDF')''')
conn.close()

