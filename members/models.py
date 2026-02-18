from django.db import models  # Import Django's ORM base classes used to define database tables

class Member(models.Model):   # Create a database model (table) named Member
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  age = models.IntegerField(null=True)
