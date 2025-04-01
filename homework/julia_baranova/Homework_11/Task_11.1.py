class Book():
    material = 'бумага'
    is_text = True

    def __init__(self, title, author, pages, ISBN, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.reserved = reserved

    def print_details(self):
        return(f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, '
                f'материал: {self.material}' f'{", зарезервирована" if self.reserved else ""}')


book_1 = Book('Идиот', 'Достоевский', '500', '978-0-6-269366-2', True)
book_2 = Book('1984', 'Оруэл', '328', '978-0-452-28423-4', False)
book_3 = Book('Мастер и Маргарита', 'Булгаков', '384', '978-0-316-76948-0', False)
book_4 = Book('Солярис', 'Лем', '224', '978-0-15-602760-1', False)
book_5 = Book('Над пропастью во ржи', 'Сэлинджер', '277', '978-5-389-7423-4', False)

print(book_1.print_details())
print(book_2.print_details())
print(book_3.print_details())
print(book_4.print_details())
print(book_5.print_details())
