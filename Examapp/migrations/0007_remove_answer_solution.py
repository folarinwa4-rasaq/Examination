# Generated by Django 5.0.6 on 2024-10-31 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Examapp', '0006_remove_question_option1_remove_question_option2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='solution',
        ),
    ]
