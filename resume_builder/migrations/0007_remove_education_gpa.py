# Generated by Django 3.0.7 on 2020-10-29 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0006_remove_contactinfo_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='gpa',
        ),
    ]
