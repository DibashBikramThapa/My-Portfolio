# Generated by Django 3.2.1 on 2021-07-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(blank=True, default='exit', upload_to='profilepic'),
            preserve_default=False,
        ),
    ]
