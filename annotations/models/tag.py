from django.db import models

class Tag(models.Model):
    label = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    
    def __str__(self):
        return self.label
