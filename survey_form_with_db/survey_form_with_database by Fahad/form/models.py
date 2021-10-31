from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    role = models.CharField(max_length=100)
    recommend = models.CharField(max_length=100)
    fav_feature = models.CharField(max_length=100)
    comments = models.CharField(max_length=500)

    def __str__(self) :
        return self.name
