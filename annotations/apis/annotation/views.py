from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AnnotationCreateSerializer


@api_view(['POST'])
def add_annotation(request):
    serializer = AnnotationCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
