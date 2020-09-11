# Generated by Django 3.0.7 on 2020-09-11 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactInfo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resume_builder.ContactInfo')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume_builder.Resume'),
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume_builder.Resume'),
        ),
        migrations.AddField(
            model_name='hobby',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume_builder.Resume'),
        ),
        migrations.AddField(
            model_name='project',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume_builder.Resume'),
        ),
        migrations.AddField(
            model_name='skill',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume_builder.Resume'),
        ),
    ]
