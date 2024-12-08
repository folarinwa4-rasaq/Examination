# Generated by Django 5.0.6 on 2024-12-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examapp', '0014_delete_studentanswers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='description',
            field=models.TextField(max_length=125),
        ),
        migrations.AlterField(
            model_name='exam',
            name='duration',
            field=models.FloatField(default=120),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.CharField(choices=[('mathematics', 'mathematics'), ('english', 'english'), ('physics', 'physics'), ('chemistry', 'chemistry'), ('biology', 'biology'), ('geography', 'geography'), ('further-mathematics', 'further-mathematics'), ('economics', 'economics'), ('agric', 'agric'), ('civic', 'civic'), ('marketing', 'marketing'), ('crs', 'crs'), ('government', 'government'), ('account', 'account'), ('commerce', 'commerce'), ('literature', 'literature'), ('yoruba', 'yoruba'), ('business-studies', 'business-studies'), ('basic-science', 'basic-science'), ('basic-technology', 'basic-technology'), ('p.h.e', 'p.h.e'), ('music', 'music'), ('french', 'french'), ('home-economics', 'home-economics'), ('c.c.a', 'c.c.a'), ('social-studies', 'social-studies'), ('security-education', 'security-education'), ('history', 'history')], max_length=50),
        ),
        migrations.AlterField(
            model_name='exam',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]