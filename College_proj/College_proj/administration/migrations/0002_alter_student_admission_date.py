# Generated by Django 4.2.6 on 2024-02-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.DateField(auto_now=True),
        ),
    ]
