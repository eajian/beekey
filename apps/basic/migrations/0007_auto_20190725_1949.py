# Generated by Django 2.2.3 on 2019-07-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_newsmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='desc',
            field=models.CharField(max_length=200, verbose_name='新闻描述'),
        ),
    ]