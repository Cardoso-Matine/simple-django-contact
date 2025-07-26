from django.db import models

# Create your models here.

from django.db import models

# Modelo simples de contato
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
