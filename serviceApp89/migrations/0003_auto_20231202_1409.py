# Generated by Django 3.2.4 on 2023-12-02 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp89', '0002_docimg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doc',
            options={'ordering': ['-publishDate'], 'verbose_name': '壁纸', 'verbose_name_plural': '壁纸'},
        ),
        migrations.AlterField(
            model_name='doc',
            name='file',
            field=models.FileField(blank=True, upload_to='Service/', verbose_name='上传壁纸'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='title',
            field=models.CharField(max_length=250, verbose_name='壁纸名称'),
        ),
        migrations.AlterField(
            model_name='docimg',
            name='doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docImgs', to='serviceApp89.doc', verbose_name='壁纸'),
        ),
        migrations.AlterField(
            model_name='docimg',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Doc/', verbose_name='壁纸预览图'),
        ),
    ]