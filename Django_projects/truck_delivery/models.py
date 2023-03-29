from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length = 256)
    #password = models.CharField(default='password', max_length=56)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # def __str__(self):
    #     return f'{self.name}'

class Trucks(models.Model):
    assign = models.CharField(max_length = 128)
    number = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    
    #having a list of Marks inside every student
    #is the same as having a student inside every Mark

    # def __str__(self):
    #     return f'{self.student} - {self.subject_name} - {self.score}'