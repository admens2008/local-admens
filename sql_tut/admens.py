from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

def generate_uuid():
	return str(uuid.uuid4())


class persons(Base):
	__tablename__ = "people"
	userID = Column("userID", String, primary_key=True, default=generate_uuid())
	firstName = Column("firstName", String)
	lastName = Column("lastName", String)
	profileName = Column("profileName", String)
	email = Column("email", String)

	def __init__(self, firstName, lastName, profileName, email):
		self.firstName = firstName
		self.lastName = lastName
		self.profileName = profileName
		self.email = email

#creating database
db = "sqlite:///admensDB.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

#create a session
Session = sessionmaker(bind=engine)
session = Session()

firstName = "Nana"
lastName = "Kwame-Bediako"
profileName = "NKB"
email = "nkb@gmail.com"

person = persons(firstName, lastName, profileName, email)
session.add(person)
session.commit()
print("User added Successfully")