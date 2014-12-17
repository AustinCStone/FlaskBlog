from app import db
from models import BlogPost
from models import User
#create database
db.create_all()

from app import db
# from models import BlogPost

# create the database and the db table
db.create_all()

# insert data
db.session.add(BlogPost("Good", "I\'m good.",1))
db.session.add(BlogPost("Well", "I\'m well.",1))
db.session.add(BlogPost("Excellent", "I\'m excellent.",1))
db.session.add(BlogPost("Okay", "I\'m okay.",1))
db.session.add(BlogPost("postgres", "we setup a local postgres instance",1))
db.session.add(User("admin","admin@admin.com","admin"))

# commit the changes
db.session.commit()