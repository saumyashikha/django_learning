# Generated by Django 3.2.3 on 2021-06-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stucmt',
            field=models.CharField(default='not available', max_length=70),
        ),
    ]
