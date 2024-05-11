from flask import Flask, render_template, request, redirect, url_for
from quote import Quote
from fileLoader import load_quotes_from_json, save_quotes_to_json
from datetime import datetime

app = Flask(__name__)


quotes_file_path = 'app\\quotes_json.json'
quotes = load_quotes_from_json(quotes_file_path)


@app.route('/')
def index():
    return render_template('index.html', quotes=quotes)


@app.route('/quote/<int:index>')
def quote(index):
    quote = quotes[index]
    return render_template('quote.html', quote=quote, index=index)


@app.route('/add_quote', methods=['GET', 'POST'])
def add_quote():
    if request.method == 'POST':
        quote_text = request.form['quote']
        book_name = request.form['book_name']
        author = request.form['author']
        add_date = request.form['add_date']

        new_quote = Quote(quote_text, book_name, author, add_date)
        quotes.append(new_quote)

        save_quotes_to_json(quotes, quotes_file_path)

        return redirect(url_for('index'))
    return render_template('add_quote.html', now=datetime.now())


@app.route('/delete_quote/<int:index>')
def delete_quote(index):
    del quotes[index]
    save_quotes_to_json(quotes, quotes_file_path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
