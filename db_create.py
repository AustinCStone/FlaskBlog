from project import db
from project.models import BlogPost
from project.models import User
#create database
db.create_all()

from project import db
# from models import BlogPost

# create the database and the db table
db.create_all()

# insert data
db.session.add(BlogPost("First Post", "First Post Content",1))
db.session.add(User("admin","admin@admin.com","admin"))

# commit the changes
db.session.commit()