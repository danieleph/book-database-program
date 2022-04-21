from models import (Base, session,
                    Book, engine)
import datetime
import csv


def menu():
    while True:
        print('''
                \nPROGRAMMING BOOKS
                \r1) Add book
                \r2) View all books
                \r3) Search for a book
                \r4) Book Analysis
                \r5) Exit''')
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''
                \rPlease choose one of the options above.
                \rA number from 1 to 5.
                \rPress enter to try again.''')





# import models
# done - main menu - add, search, analysis, exit, view
# add books to the database
# delete books
# search books
# data cleaning
# loop runs program

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    #print(split_date)
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)

    #datetime.date()

def clean_price(price_str):
    price_float = float(price_str)
    print(price_float)
    return int(price_float * 100)

def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            #Only create a book if it doesnt already exist in the database
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                #print(row)
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, published_date=date, price=price)
                session.add(new_book)
        session.commit()


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            #add book
            pass
        elif choice == '2':
            #view books
            pass
        elif choice == '3':
            # search book
            pass
        elif choice == '4':
            #book analysis
            pass
        else:
            print('GOODBYE')
            app_running=False

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    #menu()
    #app()
    add_csv()
    #print(clean_price('2.3'))

    for book in session.query(Book):
        print(book)