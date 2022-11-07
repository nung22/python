import flask_app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from pprint import pprint

DATABASE = "recipes"

class Recipe:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30_min = data['under_30_min']
        self.user_id = data['user_id']
        if 'first_name' in data:
            self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # This method will return all instances of recipe objects
    @staticmethod
    def validate_recipe(recipe:dict) -> bool:
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters.")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters.")
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes
    
    # This method will create a new recipe object with given data
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instructions, date_made, under_30_min) VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30_min)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN  WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            return Recipe(result[0])
        else:
            return False
