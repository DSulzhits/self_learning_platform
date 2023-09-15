from rest_framework.serializers import ModelSerializer
from sections.models import Tests, Section
from rest_framework.relations import SlugRelatedField

class TestsSerializer(ModelSerializer):
    class Meta:
        model = Tests
        fields = '__all__'


class TestsSectionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field="title", queryset=Section.objects.all())
    class Meta:
        model = Tests
        fields = ('id', 'section',)


class TestsQuestionSerializer(ModelSerializer):
    class Meta:
        model = Tests
        fields = ('id', 'section', 'question', 'answer',)

