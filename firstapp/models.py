from django.db import models

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = [
        ('', 'Select a gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    RELIGION_CHOICES = [
        ('', 'Select a Religion'),
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Buddist', 'Buddist'),
    ]
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)
    age=models.PositiveIntegerField()
    image=models.ImageField(upload_to='prof_pic')
    gender =models.CharField(max_length=10, choices=GENDER_CHOICES,default='')
    religion=models.CharField(max_length=10, choices=RELIGION_CHOICES,default='')
    address=models.TextField(max_length=100)

    def __str__(self):
        return self.name

    
