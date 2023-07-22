from django.db import models

# Create your models here.


class userInfo(models.Model):
    user_name = models.TextField()
    user_email = models.TextField()
    user_pass = models.TextField()
    user_phone = models.TextField()

def __str__(self):
    return self.name
