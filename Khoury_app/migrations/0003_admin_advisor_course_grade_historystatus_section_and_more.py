# Generated by Django 4.1.3 on 2022-11-30 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Khoury_app', '0002_alter_department_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '4. Departments',
            },
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '3. Advisors',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('credit', models.IntegerField(max_length=10)),
            ],
            options={
                'verbose_name_plural': '6. Courses',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '1. Grades',
            },
        ),
        migrations.CreateModel(
            name='HistoryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': '10. History Status',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
                ('instructor', models.CharField(max_length=150)),
                ('classSize', models.IntegerField(max_length=10)),
                ('term', models.IntegerField(max_length=1)),
                ('year', models.IntegerField(max_length=4)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.course')),
            ],
            options={
                'verbose_name_plural': '7. Sections',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('GPA', models.FloatField(max_length=5)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.grade')),
            ],
            options={
                'verbose_name_plural': '2. Students',
            },
        ),
        migrations.CreateModel(
            name='TicketStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': '8. Ticket Status',
            },
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name_plural': '5. Departments'},
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.section')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.ticketstatus')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.student')),
            ],
            options={
                'verbose_name_plural': '9. Tickets',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=500)),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.advisor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.student')),
            ],
            options={
                'verbose_name_plural': '12. Messages',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.section')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.historystatus')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.student')),
            ],
            options={
                'verbose_name_plural': '11. Histories',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Khoury_app.department'),
        ),
    ]
