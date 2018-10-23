# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from articlesApp.api.serializers import ArticleSerializers
from articlesApp.models import Articles


class ArticleCreateView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        Article = Articles.objects.all()
        serializer = ArticleSerializers(Article, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)