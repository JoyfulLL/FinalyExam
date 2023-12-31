# Generated by Django 3.2.4 on 2023-11-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp89', '0002_mynew_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mynew',
            options={'ordering': ['-publishDate'], 'verbose_name': '番剧动态', 'verbose_name_plural': '番剧动态'},
        ),
        migrations.AlterField(
            model_name='mynew',
            name='newType',
            field=models.CharField(choices=[('新番动态', '新番动态'), ('最新剧场', '最新剧场'), ('通知公告', '通知公告')], max_length=50, verbose_name='番剧类型'),
        ),
    ]
