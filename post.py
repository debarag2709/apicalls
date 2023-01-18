from flask import Flask, jsonify, request

app = Flask(__name__)

books_db = [
    {
        'name': 'Secret',
        'price': 250
    },
    {
        'name': 'Deep Secret',
        'price': 345
    }
]


# retrieve all the books form the local host
@app.route('/books')
def get_all_book():
    return jsonify({'books': books_db})


# retrieve one book from the local host http://127.0.0.1:5000/book/Secret

@app.route("/books/<string:name>")
def get_book(name):
    for i in books_db:
        if i['name'] == name:
            return jsonify(i)
    return jsonify({'message': 'book not found'})


if __name__ == "__main__":
    app.run(debug=True, port=8080)