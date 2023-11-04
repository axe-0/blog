from django.db import models

# Create your models here.
class Post(models.Model):
    #Default behaviour 
    title = models.CharField(max_length =140)
    category = models.CharField(max_length =140)
    body= models.TextField()
    date= models.DateTimeField()
    signature = models.CharField(max_length=140, default="AS ALWAYS - STAY FROSTY!")

def _str_(self):
    return self.title
