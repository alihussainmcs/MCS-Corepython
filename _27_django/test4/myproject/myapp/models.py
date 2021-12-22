from django.db import models

# Create your models here.
# id name description
#

# one to one  many to one many to many


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class User(models.Model):
    id = models.IntegerField(null=True)




# request id =  first_name = 'harsha' secon_name =

# one to one relation many to many one to many many to one
# PERSONS
# first_name last_name

