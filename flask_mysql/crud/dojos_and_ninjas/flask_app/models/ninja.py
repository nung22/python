from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the ninja table from our database
class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_and_ninjas').query_db(query)
        # Create an empty list to append our instances of ninjas
        ninjas = []
        # Iterate over the db results and create instances of ninjas with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( dojo_id, first_name, last_name, age, created_at, updated_at ) VALUES ( %(dojo_id)s, %(fname)s, %(lname)s, %(age)s, NOW(), NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_and_ninjas').query_db( query, data ) 