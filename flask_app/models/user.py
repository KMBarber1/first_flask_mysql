from flask_app.config.mysqlconnection import connectToMySQL

# Model file, Model class

class User:
    def __init__(self, data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# CREATE

    @classmethod
    def create(cls, data):
        query= "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        result = connectToMySQL("first_flask").query_db(query, data) 

        return result

# READ
# Read Many

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for row in results:
            users.append(cls(row))
        
        return users

# Read One

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        results = connectToMySQL("first_flask").query_db(query, data)

        return cls(results[0])

# UPDATE

    @classmethod
    def update(cls, data):
        print(data)
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL("first_flask").query_db(query, data)

# DELETE

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        connectToMySQL("first_flask").query_db(query, data)

