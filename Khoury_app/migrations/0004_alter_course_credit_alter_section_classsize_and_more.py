# Generated by Django 4.1.3 on 2022-11-30 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Khoury_app', '0003_admin_advisor_course_grade_historystatus_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='section',
            name='classSize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='section',
            name='term',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='section',
            name='year',
            field=models.IntegerField(),
        ),
    ]