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
    for book in books_db:
        if book['name'] == name:
            return jsonify(book)
    return jsonify({'message': 'book not found'})


if __name__ == "__main__":
    app.run(debug=True)



# from flask import jsonify, Flask
#
# appFlask = Flask(__name__)
#
#
# @appFlask.route('/home')
# def home():
#     return jsonify(username='eduCBA',
#                    account='Premium',
#                    validity='200 days')
#
#
# if __name__ == "__main__":
#     appFlask.run(debug=True)