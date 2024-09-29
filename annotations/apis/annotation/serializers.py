from rest_framework import serializers
from annotations.models.annotation import Annotation
from annotations.apis.tag.serializers import TagSerializer


class AnnotationSerializer(serializers.ModelSerializer):
    label = TagSerializer(many=False, read_only=True)

    class Meta:
        model = Annotation
        fields = ['start', 'end', 'label', 'annotated_text']
        read_only_fields = fields

class AnnotationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['start', 'end', 'label', 'annotated_text', 'document']

    def validate(self, data):
        if data['end'] <= data['start']:
            raise serializers.ValidationError("End must be greater than start.")
        return data
