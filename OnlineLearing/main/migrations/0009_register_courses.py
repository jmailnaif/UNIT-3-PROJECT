# Generated by Django 5.0.2 on 2024-04-12 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_course_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='courses',
            field=models.ManyToManyField(related_name='registrations', to='main.course'),
        ),
    ]
