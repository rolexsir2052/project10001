from django.db import models

# Create your models here.
class Normal(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    marks=models.IntegerField()
    mobile=models.IntegerField()
    place=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
class Google(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    marks=models.IntegerField()
    mobile=models.IntegerField()
    place=models.CharField(max_length=100)
    def __str__(self):
        return self.name