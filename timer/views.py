from django.views.decorators.http import require_POST
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from timer.models import Solve


def index(request):
    return render(request, 'timer/timer.html', {})


@require_POST
def submit(request):
    if request.is_ajax():
        return JsonResponse({'data': 3.14})
