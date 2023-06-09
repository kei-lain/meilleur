# Generated by Django 4.2 on 2023-04-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_category_journalsincategory_category_tasksincategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_created=True, default='2023-04-25'),
            preserve_default=False,
        ),
    ]
