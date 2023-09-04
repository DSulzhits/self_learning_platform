from django.contrib import admin
from sections.models import Section, Content


@admin.register(Section)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_filter = ('id',)
    ordering = ('id',)


@admin.register(Content)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'title',)
    list_filter = ('id', 'section',)
    ordering = ('id', 'section',)
