import sqlite3

try:
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO Event
                          (id, title, start, end_event, info, user_id) 
                           VALUES 
                          (2,'test2','2021-11-25 15:00','2021-11-25 16:00', 'information', 1)"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into Event table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
