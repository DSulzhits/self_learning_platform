from rest_framework.serializers import ModelSerializer
from sections.models import Section


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SectionListSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ('title',)
