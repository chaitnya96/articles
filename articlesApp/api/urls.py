from django.conf.urls import url

from articlesApp.views import ArticleCreateView
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArticleListView.as_view()),
    url(r'(?P<pk>\d+)/$', ArticleDetailView.as_view()),
    url(r'^create/$', ArticleCreateView.as_view()),
]
