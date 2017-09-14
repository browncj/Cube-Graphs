import statistics

from graphos.sources.model import ModelDataSource
from graphos.renderers.gchart import LineChart

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig

from timer.models import Solve
from .tables import SolveTable
from .apps import truncate_number


def index(request):
    return redirect('/home')


@login_required(login_url='/login')
def stats(request):
    context = {'empty': True}
    solves = Solve.objects.filter(user=request.user)
    num_solves = len(solves)
    if num_solves == 0:
        return render(request, 'track/stats.html', context)
    else:
        context['empty'] = False

    context['num_solves'] = num_solves

    times = sorted([solve.centiseconds / 100 for solve in solves])
    # dates = sorted([x.date for x in solves])
    context['mean'] = truncate_number(statistics.mean(times))
    context['median'] = truncate_number(statistics.median(times))
    context['stdev'] = truncate_number(statistics.stdev(times))
    context['low'] = truncate_number(times[0])
    context['high'] = truncate_number(times[len(times)-1])

    return render(request, 'track/stats.html', context)


@login_required(login_url='/login')
def tables(request):
    table = SolveTable(Solve.objects.all(), order_by='-date')
    RequestConfig(request).configure(table)
    return render(request, 'track/tables.html', {'table': table})


@login_required(login_url='/login')
def charts(request):
    qset = Solve.objects.all()
    data_source = ModelDataSource(qset, fields=['date', 'centiseconds'])
    chart = LineChart(data_source, html_id='chart_div', height=600, width=1100)
    return render(request, 'track/charts.html', {'chart': chart})
