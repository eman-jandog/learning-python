from flask import Blueprint, render_template, jsonify, request
from app.app import db
from app.library.models import Book

library = Blueprint('library', __name__, template_folder="templates")

@library.route('/')
def index():
    return render_template('library/index.html')

@library.route('/get', methods=['GET'])
def get_books():
    try: 
        books = Book.query.all()
        booksData = [{'bid': book.bid, 'title': book.title, 'author': book.author } for book in books]
        return jsonify({"data": booksData}), 200
    except Exception as e:
        return jsonify({"error": e}), 400

@library.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    
    try: 
        book = Book(title=title, author=author)

        db.session.add(book)
        db.session.commit()

        return jsonify({"bid": book.bid}), 201
    except Exception as e:
        return jsonify({"error": e}), 400
    
@library.route('/remove/<int:id>', methods=['DELETE'])
def remove_book(id):
    try:
        if not id: 
            raise ValueError('id value is not valid')
        book = Book.query.filter(Book.bid == int(id)).first_or_404()
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "success"}), 200
    except Exception as e:
        return jsonify({"error": e}), 400
    





