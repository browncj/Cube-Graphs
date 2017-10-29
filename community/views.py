from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return redirect('/home')

def reddit(request):
    return render(request, 'community/reddit.html', {})

def chat(request):
    return render(request, 'community/chat.html', {})