# Generated by Django 5.1.1 on 2024-09-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='number_of_responses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
