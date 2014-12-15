from app import db
from models import BlogPost

#create database
db.create_all()

#insert data
db.session.add(BlogPost("Good", "I good yo"))
db.session.add(BlogPost("well", "I well  yo"))

#commit changes
db.session.commit()