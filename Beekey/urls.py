"""Beekey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url, include
from Beekey.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from basic.views import BasicViewset, BannerViewset, NewsViewset

router = DefaultRouter()

router.register(r'basic', BasicViewset, base_name="basic")
router.register(r'banner', BannerViewset, base_name="banner")
router.register(r'news', NewsViewset, base_name="news")

urlpatterns = [
    url('xadmin/', xadmin.site.urls),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'docs/', include_docs_urls(title="文档")),
    url(r'^', include(router.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]