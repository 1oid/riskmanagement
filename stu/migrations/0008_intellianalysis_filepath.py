# Generated by Django 3.1.7 on 2021-04-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0007_intellianalysis'),
    ]

    operations = [
        migrations.AddField(
            model_name='intellianalysis',
            name='filepath',
            field=models.TextField(default='', verbose_name='文件路径'),
            preserve_default=False,
        ),
    ]
