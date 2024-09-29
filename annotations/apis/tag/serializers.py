from rest_framework import serializers
from annotations.models.tag import Tag 


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'label', 'color']
