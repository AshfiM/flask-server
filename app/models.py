from app import db
from werkzeug.security import generate_password_hash, check_password_hash

#Each class name is table name in database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique = True, nullable = False)
    password_hash = db.Column(db.String(255), nullable = False)
    
    def setPasswordHash(self, password):
        self.password_hash = generate_password_hash(password)
    
    def checkPassword(self, password):
        return check_password_hash(self.password_hash, password)

    