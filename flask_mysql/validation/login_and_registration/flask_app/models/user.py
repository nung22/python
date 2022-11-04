import flask_app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from pprint import pprint

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

DATABASE = "login_and_registration"

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.list_of_other_class_objects = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # This method will return all instances of user objects
    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True
        if len(user['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters.")
        if len(user['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters.")
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Invalid email address.")
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be longer than 8 characters.")
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash("Passwords do not match.")
        return is_valid
    
    # This method will create a new user object with given data
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            return User(result[0])
        else:
            return False
