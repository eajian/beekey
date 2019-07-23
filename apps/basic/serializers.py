from rest_framework import serializers
from .models import bannerModel, newsModel



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = bannerModel
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsModel
        fields = "__all__"