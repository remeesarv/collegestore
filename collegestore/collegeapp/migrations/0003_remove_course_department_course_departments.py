# Generated by Django 4.2.4 on 2023-08-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0002_rename_courses_course_rename_departments_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='department',
        ),
        migrations.AddField(
            model_name='course',
            name='departments',
            field=models.ManyToManyField(related_name='courses', to='collegeapp.department'),
        ),
    ]
