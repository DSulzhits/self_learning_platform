from django.db import models


class Section(models.Model):
    """Add Model Section
    (Добавлена Модель Section (Раздел))"""
    title = models.CharField(max_length=150, verbose_name="Title")
    description = models.TextField(verbose_name="Description", null=True, blank=True)


class Content(models.Model):
    """Add Model Content
    (Добавлена Модель Content (Содержимое))"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Section")
    title = models.CharField(max_length=150, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
