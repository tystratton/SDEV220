#Module 4 Lab  
#Author: Ty Stratton
#Date: 4/9/2025
#Purpose: This program is a simple web application that allows users to add, delete, and view books. Used Python interpreter to add

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    db.init_app(app)
    return app

app = create_app()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), unique=True, nullable=False)  
    publisher = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def home():
    return 'Hello World'

@app.route('/books')
def books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return jsonify(output)

@app.route('/books/<int:book_id>')
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'book': book.book_name})

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully'})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # This is for in case you want to run it without using the Python interpreter to add a book to the database
        if not Book.query.first():
            books = [
                Book(book_name="Harry Potter and the Sorcerer's Stone", author="J.K. Rowling", publisher="Bloomsbury"),
                Book(book_name="The Hobbit", author="J.R.R. Tolkien", publisher="Allen & Unwin"),
            ]
            for book in books:
                db.session.add(book)
            db.session.commit()
    app.run(debug=True)