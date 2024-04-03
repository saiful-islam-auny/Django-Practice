from django.db import models
from Musician.models import musician

# Create your models here.
class album(models.Model):
    name=models.CharField( max_length=50)
    musician=models.ForeignKey(musician,on_delete=models.CASCADE)
    release_date=models.DateField()
    
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    
    def __str__(self):
        return self.name
    


# class edit_album(models.Model):
