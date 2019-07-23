from rest_framework import serializers
from .models import basicModel, bannerModel, newsModel


class BasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = basicModel
        fields = "__all__"

		
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = bannerModel
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsModel
        fields = "__all__"