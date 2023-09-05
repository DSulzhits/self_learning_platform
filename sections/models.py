from django.db import models


class Section(models.Model):
    """Add Model Section
    (Добавлена Модель Section (Раздел))"""
    title = models.CharField(max_length=150, verbose_name="Title")
    description = models.TextField(verbose_name="Description", null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'


class Content(models.Model):
    """Add Model Content
    (Добавлена Модель Content (Содержимое))"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Section")
    title = models.CharField(max_length=150, verbose_name="Title")
    content = models.TextField(verbose_name="Content")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
