"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.contrib import admin
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('my-feed/', views.my_feed, name = 'my_feed'),
    path('<int:article_id>/', views.article_by_id, name = 'article_by_id'),
    re_path(r'^(?P<year>\d{4})/(?P<month>0[1-9]|1[0-2])/$', views.article_by_date, name = 'article_by_date'),
    path('create/', views.create_article, name = 'create_article'),
    path('topics/', views.show_topics, name = 'topics'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('my-profile/', views.user_profile, name = 'user_profile'),
    path('set-password/', views.set_password, name = 'set_password'),
    path('<int:article_id>/update/', views.update_article, name = 'update_article'),

    path('<int:article_id>/comment/', views.add_comment, name = 'add_comment'),
    path('<int:article_id>/delete/', views.delete_article, name = 'delete_article'),
    path('topics/<int:topic_id>/', views.show_topics, name = 'show_topics'),
    path('topics/<int:topic_id>/subscribe/', views.subscribe, name = 'subscribe'),
    path('topics/<int:topic_id>/unsubscribe/', views.unsubscribe, name = 'unsubscribe'),
    path('logout/', views.logout, name = 'logout')
    
]
