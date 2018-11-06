from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref = 'role')

    def __repr__(self):
        return '<Role %r>' % self.name
    __str__ = __repr__

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return  '<User %r>' % self.name
    __str__ = __repr__

    @property
    def password(self):      # to get the password, but it's illegal
        raise AttributeError('password is nor readable attribute')

    @password.setter
    def password(self,password):  # input password, generate hash code, and saved in password_hash column into database
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):  # get the password_hash from database and check with the input password
        return check_password_hash(self.password_hash,password)
