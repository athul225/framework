# Generated by Django 3.2.12 on 2025-02-20 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_ad_no_students_admno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='admno',
            new_name='admission_no',
        ),
    ]
