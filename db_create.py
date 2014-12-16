from app import db
from models import Parent
from models import Child
#create database
db.create_all()

#insert data
#db.session.add(BlogPost("Initial post", "Initial title"))
#db.session.add(User("Austin", "austinstone@utexas.edu","admin"))
#commit changes

db.session.add(Parent("Austin"))
db.session.add(Child("Alec"))
db.session.commit()