# Generated by Django 4.2 on 2023-04-24 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_goal_goal_goal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='goal',
            field=models.TextField(default='I want to learn to speak spanish'),
            preserve_default=False,
        ),
    ]
