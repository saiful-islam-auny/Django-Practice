# Generated by Django 5.0.2 on 2024-03-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
