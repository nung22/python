from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.book import Book
from flask_app.models.author import Author

#! Display All Books
@app.route('/books')
def books():
  return render_template('books.html', all_books = Book.get_all())

#! Create New Book Object And Redirect To Books Page
@app.route('/create_book')
def books():
  print(request.form)
  Book.save(request.form)
  return redirect('/books')

#! Display All Of The Authors Who Have Favorited A Given Book
@app.route('/books/<int:id>')
def show_book(id):
  data = { 'id' : id }
  return render_template('book_show.html', book = Book.get_book_by_id(data), not_favorited_by = Author.have_not_favorited(data))

#! Add A New Book To A Given Author's Favorite List
@app.route('/make_favorite_book/<int:book_id>/<int:author_id>')
def make_favorite_book(book_id, author_id):
  data = {
    'author_id' : author_id,
    'book_id' : book_id 
  }
  Author.make_favorite(data)
  return redirect(f'/books/{id}')