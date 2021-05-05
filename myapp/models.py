from django.db import models

# Create your models here.
class Orders(models.Model):
    name=models.CharField(max_length=120)
    address=models.TextField()
    itype=models.CharField(max_length=20)
    flavor=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    date=models.DateField()

    def __str__(self):
        return self.name
    

class Contacts(models.Model):
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)
    email=models.EmailField()
    feedback=models.TextField()
    date=models.DateField()