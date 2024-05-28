from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

# Dữ liệu giả lập
books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'read': False},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'read': True}
]

@app.route('/', methods=['GET'])
def get_home():
    return "Hello World"

@app.route('/books', methods=['GET'])
def get_books():
    data = books
    return render_template("books/view_book.html", books=data)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
