from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

#for the user to have access to previous scans

class Scans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scan_history')
    url = models.URLField(max_length=200)
    result = models.TextField()
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Scan for {self.url} by {self.user.username}'

# Create your models here.
