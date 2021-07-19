# from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import serializers
from .serializers import ArticleSerializer,TestonSerializer, UserSerializer
# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import APIView
# from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Article,Teston
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User



# Create your views here.


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class TestonViewset(viewsets.ModelViewSet):
    queryset = Teston.objects.all()
    serializer_class = TestonSerializer



'''


class ArticleViewset(viewsets.ViewSet):

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)    

    def retrieve(self, request, pk=None):
        querySet = Article.objects.all()
        article = get_object_or_404(querySet, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        querySet = Article.objects.all()
        article = get_object_or_404(querySet, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        querySet = Article.objects.all()
        article = get_object_or_404(querySet, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''

'''

class ArticleList(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        articles = self.get_object(id)
        serializer = ArticleSerializer(articles)
        return Response(serializer.data)

    def put(self, request, id):
        articles = self.get_object(id)
        serializer = ArticleSerializer(articles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        articles = self.get_object(id)
        articles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
def home(request):
    return HttpResponse("this is react api to wtl")
