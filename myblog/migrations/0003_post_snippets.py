# Generated by Django 3.0.8 on 2020-07-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20200723_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippets',
            field=models.CharField(default='Click title to read the blog post', max_length=255),
        ),
    ]
