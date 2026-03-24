from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    # Link each member to a specific user (owner)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname