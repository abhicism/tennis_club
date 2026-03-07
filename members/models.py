from django.db import models  # Import Django's ORM base classes used to define database tables

class Member(models.Model):   # Create a database model (table) named Member
  firstname = models.CharField(max_length=255) #text col to save first name with fixed max size
  lastname = models.CharField(max_length=255) #same like first name
  phone = models.IntegerField(null=True) #integer col that is allowed to store null in db
  joined_date = models.DateField(null=True) #date col, stored as null if value is missing
  age = models.IntegerField(null=True) #integer col to store age , allowed to store null if value is missing
  
def __str__(self):
    return f"{self.firstname} {self.lastname}"