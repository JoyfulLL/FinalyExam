# Generated by Django 3.2.4 on 2023-11-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp89', '0004_alter_resume_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2023-11-30', max_length=20, verbose_name='出生日期'),
        ),
    ]
