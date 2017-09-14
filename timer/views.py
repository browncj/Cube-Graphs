import json

from datetime import datetime

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseServerError, HttpResponseForbidden

from timer.models import Solve


def index(request):
    return render(request, 'timer/timer.html', {})


@require_POST
@login_required
def submit(request):
    if request.is_ajax():
        try:
            print('before')
            json_data = json.loads(request.body.decode('ASCII'))
            times = json_data['times']
        except Exception:
            return HttpResponseServerError('Malformed data!')


        for time in times:
            posix_time = time['date'] // 1000  # fractional seconds by default
            entry = Solve(centiseconds=time['centiseconds'],
                            date=datetime.utcfromtimestamp(posix_time),
                            scramble=time['scramble'],
                            user=request.user)
            entry.save()
        return HttpResponse(status=204)
