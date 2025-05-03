from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hey! It's your main view!!")

def my_feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page that will only contain articles on topics the user is subscribed to.")

def article_by_id(request: HttpRequest, article_id) -> HttpResponse:
    return HttpResponse("The page where the article will be displayed by ID.")

def add_comment(request: HttpRequest, article_id) -> HttpResponse:
    return HttpResponse("The address we will use to write comments to the article.")

def update_article(request: HttpRequest, article_id) -> HttpResponse:
    return HttpResponse("The page we will use to edit an existing article.")

def delete_article(request: HttpRequest, article_id) -> HttpResponse:
    return HttpResponse("The address we will use to delete the article")

def create_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The page on which we will create new articles.")

def show_topics(request: HttpRequest, topic_id = 0) -> HttpResponse:
    return HttpResponse("A page that lists all the topics on a site or a specific topic")
   
def subscribe(request: HttpRequest, topic_id) -> HttpResponse:
    return HttpResponse("Address for subscription to a specific topic")

def unsubscribe(request: HttpRequest, topic_id) -> HttpResponse:
    return HttpResponse("Address for unsubscribing from a specific topic")

def user_profile(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page with user data and a list of his subscriptions")

def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("New user registration page")

def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Page with password change")

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Page to enter the site")

def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Address for exiting the site")

def article_list(request: HttpRequest, year, month) -> HttpResponse:
    return HttpResponse("Page that will contain articles created in a specific month. If a request is not for a real date, there should be an error.")