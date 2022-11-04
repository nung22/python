from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from pprint import pprint
DATABASE = "books"

class Author:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.favorite_books = []
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DATABASE).query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # This method will retrieve the specific author with all the books they have favorited.
    @classmethod
    def get_author_by_id(cls , data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        author = cls( results[0] )
        for db_row in results:
            if db_row['books.id'] == None:
                break
            book_data = {
                    "id" : db_row["books.id"],
                    "title" : db_row["title"],
                    "num_of_pages" : db_row["num_of_pages"],
                    "created_at" : db_row["books.created_at"],
                    "updated_at" : db_row["books.updated_at"]
            }
            author.favorite_books.append( book.Book( book_data ) )
        return author
    
    # This method adds a new favorite book for an author
    @classmethod
    def make_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # This method will return all authors who have not favorited a given book
    @classmethod
    def have_not_favorited(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        results = connectToMySQL(DATABASE).query_db(query, data)
        authors = []
        for db_row in results:
            authors.append(cls(db_row))
        return authors