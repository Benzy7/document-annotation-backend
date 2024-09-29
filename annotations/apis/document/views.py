from rest_framework import viewsets
from rest_framework.response import Response
from annotations.models.document import Document
from .serializers import DocumentSerializer, DocumentCreateOrUpdateSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return DocumentCreateOrUpdateSerializer
        return DocumentSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # TODO CHECK IF CONTENT CHANGED
        instance.annotations_documents.all().delete()
        
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)