from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)