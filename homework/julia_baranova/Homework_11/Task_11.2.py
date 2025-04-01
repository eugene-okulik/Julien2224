from abc import abstractmethod, ABC


class Book(ABC):
    material = 'бумага'
    is_text = True

    def __init__(self, title, author, pages, ISBN, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.reserved = reserved

    @abstractmethod
    def print_details(self):
        pass


class SchoolTextbook(Book):

    def __init__(self, title, author, pages, ISBN, reserved, subject, class_number, exercises):
        super().__init__(title, author, pages, ISBN, reserved)
        self.subject = subject
        self.class_number = class_number
        self.exercises = exercises

    def print_details(self):
        return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, '
                f'предмет: {self.subject}, класс: {self.class_number}'
                f'{", зарезервирована" if self.reserved else ""}')


school_text_book_1 = SchoolTextbook('Алгебра', 'Иванов', '200', '978-0-6-269366-2',
                                    True, 'Математика', '9', True)
school_text_book_2 = SchoolTextbook('Геометрия', 'Петров', '328', '978-0-452-28423-4',
                                    False, 'Математика', '10', True)
school_text_book_3 = SchoolTextbook('Русский язык', 'Сидоров', '384', '978-0-316-76948-0',
                                    False, 'Русский язык', '8', False)
school_text_book_4 = SchoolTextbook('Бег', 'Козлов', '224', '978-0-15-602760-1',
                                    False, 'Физкультура', '7', False)

print(school_text_book_1.print_details())
print(school_text_book_2.print_details())
print(school_text_book_3.print_details())
print(school_text_book_4.print_details())
