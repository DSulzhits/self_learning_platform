from django.contrib import admin
from users.models import User


# Register your models here.
@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    """Register User model in Admin
    (Модель User зарегистрирована в админке"""
    list_display = ('id', 'email', 'is_active',)
    list_filter = ('id', 'email',)
    ordering = ('id',)
