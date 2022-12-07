import os
import datetime
from peewee import MySQLDatabase, InternalError as PeeweeInternalError
from repository.library import Library
from domain_models.book import Book
from files.pdf_file import PdfFile


class ConsoleLibrary:

    def add_book(self):
        os.system("cls")
        title = input("Введите название книги: ")
        year = int(input("Введите год: "))
        while year <= 0 or year > int(datetime.date.today().year):
            year = int(input("Неверно указан год: "))
        author = input("Введите автора: ")
        book = Book(title, year, author)
        change_option = input("Создать новую книгу %s? "
                              "\n 1-Создать"
                              "\n 2-Вернуться в меню "
                              "\n Введите команду (1,2): " % book)

        if change_option == '1':
            self.library.add(book=book)

    def delete_book(self):
        os.system("cls")
        book_number = input("Введите номер книги для удаления: ")
        book = self.library.get_at(book_number)
        if not book:
            input("Книга не найдена. Нажмите enter для возвращения в меню")
            return

        change_option = input("Вы уверены, что желаете удалить книгу? %s? "
                              "\n 1-Удалить "
                              "\n 2-Вернуться в меню "
                              "\n Введите команду (1,2): " % book)
        if change_option == '1':
            self.library.remove_at(book_number)
            print("Книга удалена ", book)

    def change_title(self, book_number, book):
        os.system("cls")
        title = input("Введите название книги: ")
        if title == "" or book.title == title:
            input("Книга не найдена. Нажмите enter для возвращения в меню")
            return
        book.title = title
        self.library.update_at(book_number, book)

    def change_author(self, book_number, book):
        os.system("cls")
        author = input("Введите автора книги: ")
        if author == "" or book.author == author:
            input("Книга не найдена. Нажмите enter для возвращения в меню")
            return
        book.author = author
        self.library.update_at(book_number, book)

    def change_year(self, book_number, book):
        os.system("cls")
        year = input("Введите год книги: ")
        if year == "" or book.year == year:
            input("Книга не найдена. Нажмите enter для возвращения в меню")
            return
        book.year = year
        self.library.update_at(book_number, book)

    def update_book(self):
        os.system("cls")
        book_id = input("Введите id книги для обновления: ")
        book = self.library.get_at(book_id)

        if not book:
            input("Книга не найдена. Нажмите enter для возвращения в меню")
            return

        print("Изменение книги", book)
        change_option = input("Что необходимо изменить? "
                              "\n 1-Название "
                              "\n 2-Автор "
                              "\n 3-Год "
                              "\n 4-Вернутся в меню"
                              "\n Введите команду (1-4): ")

        if change_option == "1":
            self.change_title(book_id, book)
        elif change_option == "2":
            self.change_author(book_id, book)
        elif change_option == "3":
            self.change_year(book_id, book)

        change_option == input("Изменить данные книги %s? "
                               "\n 1-Изменить "
                               "\n 2-Не изменять "
                               "\n Введите команду (1,2): " % book)
        if change_option == '1':
            self.library.remove_at(book_id)
            print("Книга обновлена ", book)

    def count_books(self):
        os.system("cls")
        books = self.library.get_all_books()
        print("Число книг в библиотеке: ", len(books))

    def find_books_by_author(self):
        os.system("cls")
        author = input("Введите автора для поиска: ")
        book = self.library.find_by_author(author)
        print("Найдено: ", book)
        return book

    def find_books_by_year(self):
        os.system("cls")
        year = input("Введите год для поиска: ")
        book = self.library.find_by_year(year)
        print("Найдено: ", book)
        return book

    def find_books_by_title(self):
        os.system("cls")
        title = input("Введите название для поиска: ")
        book = self.library.find_by_title(title)
        print("Найдено: ", book)
        return book

    def find_books(self):
        os.system("cls")
        search = input("Найти книги: "
                       "\n 1-По году "
                       "\n 2-По автору "
                       "\n 3-По названию "
                       "\n 4-Вернуься в меню "
                       "\n Введите команду (1-4): ")
        result = None
        if search == '1':
            result = self.find_books_by_year()
        elif search == '2':
            result = self.find_books_by_author()
        elif search == '3':
            result = self.find_books_by_title()
        return result

    def print_all_books(self):
        os.system("cls")
        pdf = PdfFile()
        books = self.library.get_all_books()
        pdf.save(books)

    def __init__(self):
        self.library = Library(data_base=MySQLDatabase('library',
                                                       user='nozid',
                                                       password='95135726840',
                                                       host='localhost',
                                                       port=3306))
        self.library.connect()

    def start(self):
        try:
            while True:
                os.system("cls")
                command = input(
                    'Библиотека:\n 1-добавить книгу '
                    '\n 2-удалить книгу '
                    '\n 3-изменить данные книги '
                    '\n 4-найти книгу '
                    '\n 5-число книг '
                    '\n 6-печать '
                    '\n 7-выход '
                    '\n Введите команду (1-7): ')
                if command == "7":
                    break
                elif command == '1':
                    self.add_book()
                elif command == '2':
                    self.delete_book()
                elif command == '3':
                    self.update_book()
                elif command == '4':
                    self.find_books()
                elif command == '5':
                    self.count_books()
                elif command == '6':
                    self.print_all_books()

            self.library.close()
        except PeeweeInternalError as px:
            print(str(px))
        print("Завершение программы")
