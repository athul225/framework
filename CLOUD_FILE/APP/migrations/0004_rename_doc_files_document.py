# Generated by Django 5.1.6 on 2025-03-07 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='doc',
            new_name='document',
        ),
    ]
