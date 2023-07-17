import sqlite3
from database.DatabaseHandler import *

databaseWorker.CreateDatabase()
db_isHere = databaseWorker.db_isHere
db_isHere2 = databaseWorker.db_isHere2
utilitiesList = "add, show all, show selected, delete all, debug, sell, exit"
try:
    conn = sqlite3.connect(db_isHere)
except sqlite3.OperationalError:
    conn = sqlite3.connect(db_isHere2)
cursor = conn.cursor()

def show_all():
    All = conn.execute('SELECT * FROM book_list')   
    Printer = All.fetchall()
    for index, best_seller, rating, name, buy, sell, quantity in Printer:
        if best_seller == 1:
            resultFromBestSeller = 'Yes'
        else:
            resultFromBestSeller = 'No'
        resultFromRating = rating/10
        if resultFromRating >= 10.001:
            resultFromRating = 10
        if resultFromRating <= -0.1:
            resultFromRating = 0
        print(f"index: {index},  the rating is: {resultFromRating}/10, the name is: {name},\nthe buy value is: {buy}, the sell value is: {sell}, best seller? {resultFromBestSeller}, the remain quantity is: {quantity}\n")
    loop()
def show_one():
    USER_INPUT3 = input("ID of the book?")
    cursor.execute(f'''
    SELECT code_book, is_bestseller, book_rating, book_name, book_value_buy, book_value_sell, book_quantity
    FROM book_list
    WHERE code_book = {USER_INPUT3}
''')
    Printer = cursor.fetchall()
    for index, best_seller, rating, name, buy, sell, quantity in Printer:
        if best_seller == 1:
            resultFromBestSeller = 'Yes'
        else:
            resultFromBestSeller = 'No'
        resultFromRating = rating/10
        if resultFromRating >= 10.001:
            resultFromRating = 10
        if resultFromRating <= -0.1:
            resultFromRating = 0
        print(f"index: {index},  the rating is: {resultFromRating}/10, the name is: {name},\nthe buy value is: {buy}, the sell value is: {sell}, best seller? {resultFromBestSeller}, the remain quantity is: {quantity}\n")
    loop()
def add():
    try:
        is_bestseller = int(input("[Administrative] is this book best seller? "))
        book_rating = int(input("[Adminstrative] what is the rating for this book? "))
        book_value_buy = float(input("[Adminstrative] what is the buy value for this book? "))
        book_value_sell = float(input("[Adminstrative] what is the selling value for this book? "))
        quantity = int(input(f"[Administrative] What is the quantity of the book?"))
        book_name = input("[Common] What is the name of the book? ")
        cursor.execute(f"""
        INSERT INTO book_list
        (is_bestseller, book_rating, book_name, book_value_buy, book_value_sell, book_quantity)
        VALUES
        ('{is_bestseller}', '{book_rating}', '{book_name}', '{book_value_buy}', '{book_value_sell}', '{quantity}')
        """)
        conn.commit()
        print(f"all set up! database updated with book: {book_name}")
    except ValueError:
        print("Error, you don't inserted numbers. 01")
    loop()
def debug():
    for i in range(5000):
        cursor.execute(f"""
            INSERT INTO book_list
            (is_bestseller, book_rating, book_name, book_value_buy, book_value_sell, book_quantity)
            VALUES
            ('0', '192', '??', '29.90', '50', '10')
""")
        conn.commit()
        print(f'the operation added: {i} books')
    loop()
def delete_all():
    try:
        with open("database/database.db", 'w') as file:
            file.write("")
            file.close()
            print("all deleted!")
    except FileNotFoundError: 
        with open("test/database/database.db", 'w') as file:
            file.write("")
            file.close()
            print("all deleted!")
    databaseWorker.CreateDatabase()
    print("database created!")
    
    loop()
def sell():
    USER_INPUT4 =  int(input('ID of the book? '))
    All = cursor.execute(f'''
SELECT code_book, is_bestseller, book_rating, book_name, book_value_buy, book_value_sell, book_quantity
FROM book_list
WHERE code_book = {USER_INPUT4}
''')
    for index, best_seller, rating, name, buy, sell, quantity in All:
        break
    USER_INPUT5 = int(input("how many books do you will sell? "))
    newQuantity = quantity - USER_INPUT5
    cursor.execute(f'''
UPDATE book_list
    SET book_quantity = {newQuantity}
WHERE code_book = {USER_INPUT4}
''')
    operationValue = sell*USER_INPUT5
    USER_INPUT6 = input(f"it will be {operationValue}$ proceed? (y/n) ")
    match USER_INPUT6:
        case 'y':
            conn.commit()
        case 'n':
            reversedQuantity = quantity
            cursor.execute(f'''
UPDATE book_list
    SET book_quantity = {reversedQuantity}
WHERE code_book = {USER_INPUT4}
''')
    loop()

def user_capabilities():
    USER_INPUT = input(f"Select the utilities... ({utilitiesList})\nR:")
    match USER_INPUT:
        case 'add':
            add()
        case 'show selected':
            show_one()
        case 'show all':
            show_all()
        case 'debug':
            debug()
        case 'sell':
            sell()
        case 'delete all':
            USER_INPUT2 = int(input("Sure? this action don't have backup. digit 12345678"))
            if USER_INPUT2 == 12345678:
                delete_all()
        case 'exit':
            exit(0)
        case '':
            loop()
def loop():
        user_capabilities()
loop()