from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from pprint import pprint
DATABASE = "books"

class Book:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.favorite_books = []
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # This method will retrieve the specific author with all the books they have favorited.
    @classmethod
    def get_books_favorited_by_author(cls , data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # results will be a list of book data with the author attached to each row. 
        author = cls( results[0] )
        for db_row in results:
            # Now we parse the book data to make instances of books and add them into our list.
          book_data = {
                  "id" : db_row["books.id"],
                  "title" : db_row["title"],
                  "num_of_pages" : db_row["num_of_pages"],
                  "created_at" : db_row["books.created_at"],
                  "updated_at" : db_row["books.updated_at"]
          }
          author.favorite_books.append( book.Book( book_data ) )
        return author