# Generated by Django 5.0.6 on 2024-11-01 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Examapp', '0008_rename_question_answer_quest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
