from django.shortcuts import render, redirect


def index(request):
    return redirect('/home')


def stats(request):
    return render(request, 'track/stats.html', {})


def tables(request):
    return render(request, 'track/tables.html', {})


def charts(request):
    return render(request, 'track/charts.html', {})
