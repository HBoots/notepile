# Generated by Django 4.1.6 on 2023-02-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_alter_note_created_alter_note_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
