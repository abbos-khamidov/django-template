from django.db import models

class Book(models.Model):
     title = models.CharField(max_length=100)
     author = models.CharField(max_length=100)
     genre = models.CharField(max_length=50)
     description = models.TextField(max_length=400)
     publication_date = models.DateField()
     price = models.PositiveIntegerField(default=0)
     
     def __str__(self):
         return self.title
