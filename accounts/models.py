from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Countries(models.Model):
    country_name = models.CharField(max_length=250)
    def __str__(self):
        return str(self.country_name)

class Languages(models.Model):
    language_name = models.CharField(max_length=250)
    def __str__(self):
        return str(self.language_name)

class CustomUser(AbstractUser):
    ACCOUNTTYPES = [('T', 'Tourist'), ('G', 'Guide')]
    country = models.ForeignKey(Countries, related_name='country', on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Languages, related_name='language', on_delete=models.CASCADE, null=True)
    account_type = models.CharField(max_length=250, choices=ACCOUNTTYPES)

