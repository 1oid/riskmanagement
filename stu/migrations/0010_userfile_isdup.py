# Generated by Django 3.1.7 on 2021-04-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0009_cachefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfile',
            name='IsDup',
            field=models.IntegerField(default=0, verbose_name='是否重复'),
        ),
    ]
