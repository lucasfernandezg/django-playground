from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
