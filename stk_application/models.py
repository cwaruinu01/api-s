from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
