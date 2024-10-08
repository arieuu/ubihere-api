# Generated by Django 5.1.1 on 2024-09-03 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter_name', models.CharField(max_length=255)),
                ('comment_owner_email', models.EmailField(max_length=255)),
                ('content', models.TextField()),
                ('project_id', models.IntegerField()),
            ],
        ),
    ]
