from django.urls import path, include
from rest_framework.routers import DefaultRouter
from annotations.apis import DocumentViewSet, TagViewSet, add_annotation

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add-annotation/', add_annotation, name='add-annotation'),
]