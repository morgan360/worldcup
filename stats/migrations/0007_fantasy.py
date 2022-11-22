# Generated by Django 4.1.3 on 2022-11-20 16:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_match_rename_country1_history_team1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fantasy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('class_year', models.CharField(max_length=30)),
                ('score1', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('score2', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.match')),
            ],
        ),
    ]