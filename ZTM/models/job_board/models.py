from django.db import models

# Create your models here.
# model => python class
# model represents a table in the database
# attributes are the fields in the table
# we want to create a job posting table
#we want to store thigs like title, description, company, salary (attributes)
# id fields are created by default; starts at 1 and autoincrements

class JobPosting(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	company = models.CharField(max_length=100)
	salary = models.FloatField()
	is_active = models.BooleanField(default=False)

#makemigrations
##creates instructions telling django how the db have changed

#migrate
##apply the changes

#CRUD Operations
##Create
##Read
##Update
##Delete

# model manager -> objects
# JobPosting.objects.all()
# JobPosting.objects.get(id=1)
# JobPosting.objects.filter(company="admens")
