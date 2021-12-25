import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect

CLIENTQUERY = """CREATE TABLE IF NOT EXISTS clients (
    id integer PRIMARY KEY,
    fname text NOT NULL,
    lname text NOT NULL,
    phone_number NUMERIC(10) NOT NULL
);
"""
CARQUERY = """CREATE TABLE IF NOT EXISTS cars (
    id integer PRIMARY KEY,
    registration CHAR(7) NOT NULL,
    model VARCHAR(25) NOT NULL,
    price NUMBER NOT NULL,
    id_client integer,
    FOREIGN KEY (id_client) REFERENCES clients(id)
);
"""

def create_connection(db_file):
    '''Creating a Database connection to a SQLite Database'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

INSERT_CAR = "INSERT INTO cars (registration, model, price, id_client) VALUES('abcdefg', 'Visa', 1200, 4)" 
SELECT_CAR = "SELECT * FROM cars"
GROUPQUERY = """
SELECT
    count(registration)
FROM
    cars
WHERE
    price BETWEEN 1000 AND 1500
GROUP BY
    model;
"""
def execute_query(conn, sql_query):
    try:
        cur = conn.cursor()
        cur.execute(sql_query)
        conn.commit()
    except Error as e:
        print(e)
    return cur
    

def fetch_rows(conn, sql_query):
    print("fetch")
    cur = execute_query(conn, sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    connection = create_connection('./Unit 01/Notes/DB practice/cars.db')
    fetch_rows(connection, GROUPQUERY)