from django.urls import path
from . import views
urlpatterns = [
    path('blog_index/',views.blog_index,name='blog_index'),
    path('blog_detail/<int:postid>/',views.blog_detail,name='blog_detail'),
    path('blog_category/<str:category>/',views.blog_categories,name='blog_category')
]