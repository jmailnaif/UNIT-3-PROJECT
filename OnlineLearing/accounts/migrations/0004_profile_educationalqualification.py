# Generated by Django 5.0.2 on 2024-04-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Educationalqualification',
            field=models.CharField(default=1, max_length=2048),
            preserve_default=False,
        ),
    ]
