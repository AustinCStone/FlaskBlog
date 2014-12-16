from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


'''class BlogPost(db.Model):
    __tablename__="posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    #temp_var = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, title, description):
        self.title=title
        self.description=description

    def __repr__(self):
        return '{}|{}'.format(self.title,self.description)

class User(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    author_posts = relationship("BlogPost",backref="users")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<name {}'.format(self.name)
  '''

class Parent(db.Model):
    __tablename__ = 'parent'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    children = relationship("Child", backref="parent")
    def __init__(self, name):
        self.name = name


class Child(db.Model):
    __tablename__ = 'child'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    parent_id = db.Column(db.Integer, ForeignKey('parent.id'))
    def __init__(self, name):
        self.name = name