# Generated by Django 4.1.13 on 2024-11-25 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_note_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
