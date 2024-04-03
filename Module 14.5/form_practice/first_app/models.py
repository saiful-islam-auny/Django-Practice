from django.db import models
from datetime import datetime
from datetime import date

class Student(models.Model):
    roll = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 20)
    address = models.TextField()
    birth_date = models.DateField(default= date.today())
    boolean_field = models.BooleanField(default= False)
    date_time_field = models.DateTimeField(default=datetime.now)
    email_field = models.EmailField(default='hello@gmail.com')
    image_field = models.ImageField(default='img.jpg')
    def __str__(self):
        return f"Roll : {self.roll} - {self.name}"