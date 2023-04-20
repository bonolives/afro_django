from django.db import models

# Create your models here.

# we are creating our own custom user model instead of django custom model hence the "user_account"
class User_account(models.Model):
    username = models.CharField(max_length=22)
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=22)
    signup_time = models.DateTimeField(auto_now=True)

class About_form(models.Model):
    username= models.CharField(max_length=22, null= True, blank= True)
    gender = models.CharField(max_length=6, null= True, blank= True)
    email = models.CharField(max_length=30, null= True, blank= True)    
    course= models.CharField(max_length = 50, null = True, blank = True)
    cohort = models.CharField(max_length = 10, null = True, blank = True)
    university = models.CharField(max_length=40, null=True, blank= True)    




    