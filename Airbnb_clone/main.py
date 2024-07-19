import json
from uuid import uuid4
class Person:
	def __init__(self, name, age) -> None:
		self.id = str(uuid4())
		self.name = name
		self.age = age
		

	def __str__(self):
		return f"id: {self.id}, name: {self.name}, age: {self.age}"
	
	# def save(self):
	# 	with open("file.json", "a") as file:
	# 		file.write(str(self))
	# 		file.write("\n")

	def to_dict(self):
		return self.__dict__
	
	def new(self):
		key = f"{self.__class__.__name__}.{self.id}"
		return key

	def save(self):
			serialized_obj = {}
			serialized_obj[self.new()] = self.to_dict()
			with open("file.json", "w") as file:
				json.dump(serialized_obj, file, indent=4)
		
#Initiate our class
person1 = Person("Isaac", 40)
person2 = Person("Joe", 38)
# person3 = Person("Sarah", 26, "Female")

# print(person1)
# print(person2)
# print(person1.to_dict())

person1.save()
person2.save()
# person3.save()