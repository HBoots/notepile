# Generated by Django 4.1.6 on 2023-02-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='fragment',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
