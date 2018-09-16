from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from articlesApp.models import Articles
from .serializers import ArticleSerializers


class ArticleListView(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializers
