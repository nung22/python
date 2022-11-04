from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from pprint import pprint
DATABASE = "books"

class Book:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.num_of_pages = db_data['num_of_pages']
        self.favorited_by_author = []
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of books
        books = []
        # Iterate over the db results and create instances of books with cls.
        for book in results:
            books.append( cls(book) )
        return books
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books ( title, num_of_pages, created_at , updated_at ) VALUES (%(title)s,%(num_of_pages)s,NOW(),NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # This method will retrieve the specific book with all the authors who favorited it.
    @classmethod
    def get_book_favorited_by_authors( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # results will be a list of author objects with the book attached to each row. 
        book = cls( results[0] )
        for db_row in results:
            # Now we parse the author data to make instances of authors and add them into our list.
            author_data = {
                    "id" : db_row["authors.id"],
                    "name" : db_row["name"],
                    "created_at" : db_row["authors.created_at"],
                    "updated_at" : db_row["authors.updated_at"]
            }
            book.favorited_by_author.append( author.Author( author_data ) )
        return book