from fileLoader import load_quotes_from_json, save_quotes_to_json
from quote import Quote

def  main():
    quotes_file_path = 'quotes_json.json'
    quotes = load_quotes_from_json(quotes_file_path)

    print(type(quotes))
    for i in quotes:
        print(type(i))
    print(quotes)

if __name__ == '__main__':
    main()