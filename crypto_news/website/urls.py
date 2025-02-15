from django.contrib import admin
from django.urls import path, include
from website import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('home/', views.index, name='home'),
    path("about_us/", views.about, name='about_us'),
    path("about_us/", views.create_news, name='create_news'),
    
    path('news/', views.news, name="news"),
    path('analysis/', views.analysis, name="analysis"),
    path('analysis/<int:pk>/', views.view_full_Article, name="view_full_Article"),
    path('news/<int:pk>/', views.view_full_News, name="view_full_News"),

    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    
]