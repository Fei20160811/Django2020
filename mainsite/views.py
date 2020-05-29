from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.
def homepage(request):
    template = get_template("index.html")
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, id):
    template = get_template("post.html")
    try:
        post = Post.objects.get(id=id)
        if post:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect("/")