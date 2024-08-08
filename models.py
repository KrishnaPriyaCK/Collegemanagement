from django.db import models

class studentreg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    number = models.CharField(max_length=200)
    age = models.IntegerField()
    enrollmentdate = models.DateField()
    course = models.CharField(max_length=100)

