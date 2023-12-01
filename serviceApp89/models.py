from django.db import models

import django.utils.timezone as timezone
# Create your models here.


class Doc(models.Model):
    title = models.CharField(max_length=250, verbose_name='壁纸名称')
    file = models.FileField(upload_to='Service/',
                            blank=True,
                            verbose_name='上传壁纸')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "壁纸"
        verbose_name_plural = verbose_name


class DocImg(models.Model):
    doc = models.ForeignKey(Doc,
                                related_name='docImgs',
                                verbose_name='壁纸',
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Doc/',
                              blank=True,
                              verbose_name='壁纸预览图')
    class Meta:
        verbose_name = '壁纸'
        verbose_name_plural = '壁纸'
