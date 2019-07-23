from django.shortcuts import render

from rest_framework import mixins
from rest_framework import viewsets
# Create your views here.
from .models import basicModel, bannerModel, newsModel
from .serializers import BasicSerializer, BannerSerializer, NewsSerializer


class BasicViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取轮播图列表
    """
    queryset = basicModel.objects.all()
    serializer_class = BasicSerializer

class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取轮播图列表
    """
    queryset = bannerModel.objects.filter(state=True).order_by("index")
    serializer_class = BannerSerializer

class NewsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取新闻列表
    """
    queryset = newsModel.objects.filter(is_hot=True)
    serializer_class = NewsSerializer