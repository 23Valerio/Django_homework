from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('my_feed/', views.my_feed, name = 'my_feed'),
    path('<int:article_id>/', views.article, name = 'article_by_id'),


    re_path(r'^(?P<year>\d{4})/(?P<month>0[1-9]|1[0-2])/$', views.article_by_date, name = 'article_by_date'),
    path('create/', views.create_article, name = 'create_article'),
    path('topics/', views.show_topics, name = 'topics'),
    path('topics/<int:topic_id>/', views.articles_by_topic, name = 'articles_by_topic'),
    path('login/', views.my_login, name = 'login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name = 'register'),
    path('my-profile/', views.user_profile, name = 'user_profile'),
    path('set-password/', views.set_password, name = 'set_password'),
    path('<int:article_id>/update/', views.update_article, name = 'update_article'),

    path('<int:article_id>/comment/', views.add_comment, name = 'add_comment'),
    path('<int:article_id>/delete/', views.delete_article, name = 'delete_article'),
   
    path('topics/<int:topic_id>/subscribe/', views.subscribe, name = 'subscribe'),
    path('topics/<int:topic_id>/unsubscribe/', views.unsubscribe, name = 'unsubscribe'),
    
    
]
