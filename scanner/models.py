from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

#for the user to have access to previous scans

class ScanResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    results = models.JSONField()
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.url} scanned at {self.scanned_at}'

# Create your models here.
