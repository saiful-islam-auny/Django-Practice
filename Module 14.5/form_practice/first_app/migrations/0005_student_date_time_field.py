# Generated by Django 5.0.2 on 2024-03-29 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_student_boolean_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_time_field',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
