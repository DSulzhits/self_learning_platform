# Generated by Django 4.2.4 on 2023-09-12 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
