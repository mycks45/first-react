from django.contrib import admin
from django.urls import path,include
from .views import ArticleViewset, TestonViewset, UserViewset
from rest_framework.routers import DefaultRouter

#ArticleList,ArticleDetails

router = DefaultRouter()
router.register('articles', ArticleViewset, basename='articles')
router.register('users', UserViewset, basename='users')
router.register('test', TestonViewset, basename='test')


urlpatterns = [

    path('api/', include(router.urls)),
    


#     path('articles/', ArticleList.as_view() , name='article'),
#     path('articles/<int:id>/', ArticleDetails.as_view() , name='ArticleDetails')
 ]
