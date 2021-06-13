from django.db import models


class Profile(models.Model):
    email = models.CharField(max_length=300)
    phone_no = models.CharField(max_length=300)

