from flask_app.models import ninja
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the dojos table from our database
class Dojo:
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_and_ninjas').query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"
        # results will be a list of info with the ninja attached to each row
        results = connectToMySQL('dojo_and_ninjas').query_db( query, data )
        # print(results)
        dojo = cls(results[0])
        # parse the ninja info to make instances of ninjas and add them to the list
        for row_from_db in results:
            ninja_data = {
                'id' : row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'created_at' : row_from_db['ninjas.created_at'],
                'updated_at' : row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        print(dojo)
        return dojo

    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW(), NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_and_ninjas').query_db( query, data )