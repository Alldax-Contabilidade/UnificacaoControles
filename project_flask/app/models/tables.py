from project_flask.app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    department = db.relationship('Department', foreign_keys=department_id)

    def __init__(self, username, password, name, email, department_id):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.department_id = department_id

    def __repr__(self):
        return "<User %r>" % self.username


class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name_departmanet = db.Column(db.String, unique=True)

    def __init__(self, name_departament):
        self.name_departmanet = name_departament

    def __repr__(self):
        return "<Department %r>" % self.id


class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    user = db.relationship('User', foreign_keys=user_id)
    department = db.relationship('Department', foreign_keys=department_id)

    def __init__(self, content, user_id, department_id):
        self.content = content
        self.user_id = user_id
        self.department_id = department_id

    def __repr__(self):
        return "<Ativity %r>" % self.id

