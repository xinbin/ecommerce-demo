from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.filter(status=Article.ACTIVE)
    return render(request, "blog/index.html", {'articles': articles})


def article(request, aid):
    blog = Article.objects.get(id=aid)
    return render(request, "blog/article.html", {'blog': blog})

