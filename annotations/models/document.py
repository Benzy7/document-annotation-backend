from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content  = models.TextField()
