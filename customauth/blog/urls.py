from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.blog_create, name='blog_create'),  # specific URL top
    path('<slug:slug>/edit/', views.blog_edit, name='blog_edit'),
    path('<slug:slug>/delete/', views.blog_delete, name='blog_delete'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),  # slug URL last
    path('', views.blog_list, name='blog_list'),  # list page at end or top depending
]