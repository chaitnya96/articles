from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from articlesApp.models import Articles
from .serializers import ArticleSerializers
from rest_framework.viewsets import ModelViewSet


class ArticleListView(ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializers

