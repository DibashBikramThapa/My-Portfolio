# Generated by Django 3.2.5 on 2021-07-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0007_aboutme_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
    ]
