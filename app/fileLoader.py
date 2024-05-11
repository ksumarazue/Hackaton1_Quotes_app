import json
from quote import Quote


def load_quotes_from_json(file_path):
    with open(file_path, 'r') as file:
        quotes_data = json.load(file)
    quotes_list = []
    for quote_data in quotes_data:
        # print(type(quote_data))
        quote_object = Quote(quote_data['quote'], quote_data['add_date'], quote_data['book_name'], quote_data['author'])
        quotes_list.append(quote_object)
    return quotes_list


def save_quotes_to_json(quotes, file_path):
    with open(file_path, 'w') as file:
        quotes_dict_list = []
        for quote in quotes:
            quote_dict = quote.__dict__
            quotes_dict_list.append(quote_dict)
        json.dump(quotes_dict_list, file, indent=4)
