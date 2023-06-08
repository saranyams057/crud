from django.db import models

# Create your models here.


# Create your models here.
class Crud(models.Model):
    slno = models.IntegerField()
    itemname = models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    def __str__(self):
        return self.itemname