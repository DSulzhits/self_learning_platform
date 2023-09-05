from rest_framework.serializers import ModelSerializer
from sections.models import Content, Section
from rest_framework.relations import SlugRelatedField

"""Add serializers for Content views
(Добавлены сериализаторы для контроллеров Content)"""


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class ContentListSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field="title", queryset=Section.objects.all())

    class Meta:
        model = Content
        fields = ('id', 'section', 'title',)
