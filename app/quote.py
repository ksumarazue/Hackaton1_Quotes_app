
class Quote():
    def __init__(self, quote, add_date, book_name = 'Brak danych', author = 'Brak danych'):
        self.quote = quote
        self.book_name = book_name
        self.author = author
        self.add_date = add_date

    def __str__(self):
        return f'Quote: "{self.quote}" - {self.author}, {self.book_name}, added on {self.add_date}'