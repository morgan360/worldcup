# Generated by Django 4.1.3 on 2022-11-20 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0012_alter_fantasy_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fantasy',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.match', unique=True),
        ),
    ]
