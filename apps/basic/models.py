from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
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
    is_open = models.BooleanField(default=False, verbose_name="是否开启", help_text="系统只取开启的第一个条数据为准")
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

# class indexNewsModel(models.Model):
#     category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True, verbose_name="商品类目")
#     update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

#     class Meta:
#         verbose_name = '首页新闻'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.name

class newsModel(models.Model):
    name =  models.CharField(max_length=100, verbose_name="新闻标题")
    desc = models.CharField(max_length=200, verbose_name="新闻描述")
    image = models.ImageField(upload_to='news/', verbose_name="新闻封面")
    content = UEditorField(verbose_name=u"内容", imagePath="news/images/", width=1000, height=300, filePath="news/files/", default='')
    is_hot = models.BooleanField(default=True, verbose_name="是否展示")
    time = models.CharField(max_length=100, verbose_name="新闻时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '新闻列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name