# Generated by Django 4.1.3 on 2022-11-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0008_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fantasy',
            name='class_year',
        ),
        migrations.RemoveField(
            model_name='fantasy',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='fantasy',
            name='last_name',
        ),
        migrations.AddField(
            model_name='fantasy',
            name='student',
            field=models.CharField(default='N/A', max_length=60),
        ),
    ]
