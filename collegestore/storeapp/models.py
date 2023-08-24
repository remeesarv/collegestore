from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=200,unique=True)
    link = models.URLField()

    def __str__(self):
        return '{}'.format(self.name)



