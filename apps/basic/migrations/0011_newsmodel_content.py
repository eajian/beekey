# Generated by Django 2.2.3 on 2019-07-25 20:12

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0010_remove_newsmodel_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
    ]