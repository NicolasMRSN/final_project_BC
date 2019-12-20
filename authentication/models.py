from django.db import models

# Create your models here.
class User(models.Model):
    """Application user database.
    """
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    wallet_id = models.CharField(max_length=42)