# Generated by Django 3.2.25 on 2025-02-12 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='previousEmployeer',
            new_name='previousEmployer',
        ),
    ]
