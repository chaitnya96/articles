from rest_framework import serializers

from articlesApp.models import Articles


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
