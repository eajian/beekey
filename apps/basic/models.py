from django.db import models
from datetime import datetime
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill

# Create your models here.
class basicModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="站点名称")
    logoPic = models.ImageField(upload_to="logo/", verbose_name="Logo")
    companyName = models.CharField(max_length=100, verbose_name="公司名称")
    companyAdress = models.CharField(max_length=100, verbose_name="公司地址")
    companyLink = models.CharField(max_length=100, verbose_name="联系人")
    companyLinkPhone = models.CharField(max_length=100, verbose_name="联系电话/微信")
    companyEmail = models.EmailField(verbose_name="邮箱地址")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "站点设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class bannerModel(models.Model):
    name =  models.CharField(max_length=100, verbose_name="轮播描述")
    image = models.ImageField(upload_to='banner/', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序", help_text="数字越小在越前面")
    state = models.BooleanField(default=True, verbose_name="是否展示")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class newsModel(models.Model):
    name =  models.CharField(max_length=100, verbose_name="新闻标题")
    desc = models.TextField(max_length=200, verbose_name="新闻描述")
    image = models.ImageField(upload_to='news/', verbose_name="新闻封面")
    is_hot = models.BooleanField(default=True, verbose_name="是否展示")
    time = models.CharField(max_length=100, verbose_name="新闻时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '新闻列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name