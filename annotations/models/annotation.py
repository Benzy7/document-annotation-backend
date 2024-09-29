from django.db import models

class Annotation(models.Model):
    document = models.ForeignKey("Document", related_name='annotations_documents', on_delete=models.CASCADE)
    label = models.ForeignKey("Tag", related_name='annotations_labels', on_delete=models.CASCADE)
    start = models.IntegerField()
    end = models.IntegerField()
    annotated_text = models.CharField(max_length=255)
    
    class Meta:
        unique_together = ('start', 'end', 'document')

    def __str__(self):
        return f"{self.document}-{self.label}"
