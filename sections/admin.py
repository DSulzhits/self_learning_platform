from django.contrib import admin
from sections.models import Section, Content


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """Register Section model in Admin
    (Модель Section зарегистрирована в админке)"""
    list_display = ('id', 'title',)
    list_filter = ('id',)
    ordering = ('id',)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    """Register Content model in Admin
    (Модель Content зарегистрирована в админке)"""
    list_display = ('id', 'section', 'title',)
    list_filter = ('id', 'section',)
    ordering = ('id', 'section',)
