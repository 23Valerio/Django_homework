from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request):
    return render(request, 'index.html')

def my_feed(request):
    return render(request, 'my_feed.html')

def article_by_id(request, article_id = 0):
    return render(request, 'article_by_id.html', {'article_id': article_id})

def create_article(request):
    return render(request, 'create_article.html')

def show_topics(request, topic_id = 0):
    return render(request, 'topics.html', {'topic_id': topic_id})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def set_password(request):
    return render(request, 'set_password.html')

def article_by_date(request, year, month):
    return render(request, 'article_by_date.html', {'year': year, 'month': month})

def update_article(request, article_id = 0):
    return render(request, 'update_article.html', {'article_id': article_id})



def add_comment(request: HttpRequest, article_id) -> HttpResponse:
    return HttpResponse("The address we will use to write comments to the article.")

def delete_article(request: HttpRequest, article_id) -> HttpResponse:
    return HttpResponse("The address we will use to delete the article")
  
def subscribe(request: HttpRequest, topic_id) -> HttpResponse:
    return HttpResponse("Address for subscription to a specific topic")

def unsubscribe(request: HttpRequest, topic_id) -> HttpResponse:
    return HttpResponse("Address for unsubscribing from a specific topic")






def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Address for exiting the site")

