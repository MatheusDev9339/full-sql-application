import sqlite3
db_isHere = 'database/database.db'
db_isHere2 = 'test/database/database.db'
class databaseWorker:
    db_isHere = 'database/database.db'
    db_isHere2 = 'test/database/database.db'
    def CreateDatabase():
        try:
            conn = sqlite3.connect(db_isHere)
        except sqlite3.OperationalError:
            conn = sqlite3.connect(db_isHere2)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS book_list (
            code_book       INTEGER PRIMARY KEY,
            is_bestseller   INTEGER NOT     NULL,
            book_rating     INTEGER NOT     NULL, 
            book_name       TEXT    NOT     NULL,
            book_value_buy  INTEGER NOT     NULL,
            book_value_sell INTEGER NOT     NULL,
            book_quantity   INTEGER NOT     NULL)
''')
    CreateDatabase()