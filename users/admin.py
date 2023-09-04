from django.contrib import admin
from users.models import User


# Register your models here.
@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    """"""
    list_display = ('id', 'email', 'is_active',)
    list_filter = ('id', 'email',)
    ordering = ('id',)
