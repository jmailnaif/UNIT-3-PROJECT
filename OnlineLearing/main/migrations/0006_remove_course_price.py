# Generated by Django 5.0.2 on 2024-04-12 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_course_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
    ]
