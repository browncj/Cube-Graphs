from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'timer/timer.html', {})

def submit(request):
    if request.method == 'POST':
        return HttpResponse('I got a post')
    else:
        return HttpResponse('something')
