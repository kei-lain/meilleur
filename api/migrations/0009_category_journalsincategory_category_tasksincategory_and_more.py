# Generated by Django 4.2 on 2023-04-25 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='journalsInCategory',
            field=models.ManyToManyField(null=True, to='api.journal'),
        ),
        migrations.AddField(
            model_name='category',
            name='tasksInCategory',
            field=models.ManyToManyField(null=True, to='api.task'),
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryName',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='goalsInCategory',
            field=models.ManyToManyField(null=True, to='api.goal'),
        ),
    ]
