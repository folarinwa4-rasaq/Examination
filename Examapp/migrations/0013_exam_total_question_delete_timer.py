# Generated by Django 5.0.6 on 2024-11-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examapp', '0012_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='total_question',
            field=models.IntegerField(default=60),
        ),
        migrations.DeleteModel(
            name='Timer',
        ),
    ]
