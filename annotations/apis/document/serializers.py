from rest_framework import serializers
from annotations.models.document import Document
from annotations.apis.annotation.serializers import AnnotationSerializer


class DocumentSerializer(serializers.ModelSerializer):
    annotations = AnnotationSerializer(source='annotations_documents', many=True, read_only=True)
    
    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'annotations']
        read_only_fields = fields
        
class DocumentCreateOrUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ['title', 'content']
