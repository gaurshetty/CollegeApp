from django.db import models

class Student(models.Model):
    name = models.CharField('name', max_length=100)
    age = models.IntegerField('age')
    fees = models.FloatField('fees')
    address = models.CharField('address', max_length=100)

# s1 = Student(name='shetty', age=30, fees=25000, address='Pune')

