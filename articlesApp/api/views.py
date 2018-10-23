from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from articlesApp.models import Articles
from .serializers import ArticleSerializers


class ArticleListView(ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = (AllowAny,)


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializers

