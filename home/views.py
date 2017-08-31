from django.shortcuts import render

from home.models import Post


def index(request):
    posts = Post.objects.order_by('-created_date')
    context = {'posts': posts}
    return render(request, 'home/home.html', context)
