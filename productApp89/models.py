from django.db import models
from django.shortcuts import get_object_or_404, render

# Create your models here.
from django.utils import timezone


class Product(models.Model):
    PRODUCTS_CHOICES = (
        ('哆啦道具', '哆啦道具'),
    )
    title = models.CharField(max_length=50, verbose_name='道具名称')
    description = models.TextField(verbose_name='产品详细秒速')
    productType = models.CharField(
        choices=PRODUCTS_CHOICES,
        max_length=50,
        verbose_name='道具类型')
    price = models.DecimalField(
        max_digits=7, decimal_places=1, blank=True, null=True, verbose_name='道具价格')
    publishDate = models.DateTimeField(
        max_length=20, default=timezone.now, verbose_name='发布时间')

    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '道具'
        verbose_name_plural = '道具'
        ordering = ('-publishDate',)



class ProductImg(models.Model):
    product = models.ForeignKey(
        Product, related_name='productImgs', verbose_name='道具', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Product/',
                              blank=True, verbose_name='道具图片')

    class Meta:
        verbose_name = '道具图片'
        verbose_name_plural = '道具图片'

