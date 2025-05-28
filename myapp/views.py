from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from myapp.models import Article, Topic
from .forms import AuthenticationForm, RegistrerForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    articles = Article.objects.all().order_by('-created_at').prefetch_related('topics')
    return render(request, 'index.html', {"articles": articles})

@login_required
def my_feed(request):
        if request.user.is_authenticated:
            articles = Article.objects.filter(topics__subscribers=request.user).order_by('-created_at').select_related('autor').prefetch_related('topics').distinct()
        else:
            articles = Article.objects.all().order_by('-created_at').prefetch_related('topics')
        return render(request, 'my_feed.html', {"articles": articles})

def article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return redirect('index')
    return render(request, 'article_by_id.html', {'article': article})

def create_article(request):
    return render(request, 'create_article.html')

def show_topics(request):
    topics = Topic.objects.all()
    return render(request, 'topics.html', {'topics': topics})

def articles_by_topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Article.DoesNotExist:
        return redirect('topics')
    articles = Article.objects.filter(topics=topic_id).prefetch_related('topics').order_by('-created_at')
    return render(request, 'articles_by_topic.html', {'articles': articles})


def my_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)
        # check validity:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            login(request, form.user)
            return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegistrerForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('index')
    else:
        form = RegistrerForm()
    return render(request, 'register.html', {'form': form})

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