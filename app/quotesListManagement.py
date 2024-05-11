from quote import Quote
class QuotesListManagement:
    def __init__(self, data):
        self.quotes_list = []
        for quote_data in data:
            quote_obj = Quote(quote_data['quote'], quote_data['Book_name'], quote_data['author'], quote_data['add_date'])
            self.quotes_list.append(quote_obj)

    def __str__(self):
        return "\n".join(str(quote) for quote in self.quotes_list)