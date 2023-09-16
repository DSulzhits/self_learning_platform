from rest_framework.serializers import ModelSerializer
from sections.models import Tests, Section
from rest_framework.relations import SlugRelatedField


class TestsSerializer(ModelSerializer):
    test_section = SlugRelatedField(slug_field="title", queryset=Section.objects.all())

    class Meta:
        model = Tests
        fields = ('id', 'test_section',)


class TestsQuestionSerializer(ModelSerializer):
    test_section = SlugRelatedField(slug_field="title", queryset=Section.objects.all())

    class Meta:
        model = Tests
        fields = ('id', 'test_section', 'question', 'answer',)
