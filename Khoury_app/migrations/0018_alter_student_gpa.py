# Generated by Django 4.1.3 on 2022-12-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Khoury_app', '0017_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='GPA',
            field=models.FloatField(default=4.0, max_length=5),
        ),
    ]