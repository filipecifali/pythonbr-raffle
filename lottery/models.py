from django.db import models

class Person(models.Model):
    """A user registered for the raffle."""
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Registration(models.Model):
    """Emails registered on the event."""
    email = models.EmailField(primary_key=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)
      