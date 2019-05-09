from django.db import models

class ContactData(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    cources=models.CharField(max_length=50)

class FeedbackData(models.Model):
    name=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
    time=models.DateField(max_length=50)
    feedback=models.CharField(max_length=200)
