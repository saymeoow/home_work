import sqlite3


def create_tables(conn: sqlite3.Connection):
    curs = conn.cursor()
    curs.execute("""CREATE TABLE IF NOT EXIST department(
    name TEXT
    manager_id INTEGER PRIMARY KEY AUTOINCREMENT
    location_id INTEGER PRIMARY KEY AUTOINCREMENT
);""")
    conn.commit()
    return curs.fetchall()

def insert_info_to_table(conn: sqlite3.Connection):
    curs = conn.cursor()
    curs.execute("""
    INSERT INTO department (name)
    VALUES
    ('John'),
    ('Sasha'),
    ('Vlad')
    """)
    conn.commit()
    return curs.fetchall()

def get_data(conn: sqlite3.Connection):
    curs = conn.cursor()
    curs.execute("""INSERT * INTO department""")
    conn.commit()
    return curs.fetchall()

def main():
    conn = sqlite3.connect('table.db')
    try:
        create_tables(conn)
        insert_info_to_table(conn)
        data = get_data(conn)
        print(data)

    except:
        conn.close()


main()
