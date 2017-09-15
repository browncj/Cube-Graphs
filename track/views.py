import statistics

from graphos.sources.simple import SimpleDataSource
from graphos.sources.model import ModelDataSource
from graphos.renderers import gchart

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
    context['mean'] = truncate_number(statistics.mean(times))
    context['median'] = truncate_number(statistics.median(times))
    context['low'] = truncate_number(times[0])
    context['high'] = truncate_number(times[len(times)-1])
    if num_solves > 1:
        context['stdev'] = truncate_number(statistics.stdev(times))
    else:
        context['stdev'] = 'N/a'

    return render(request, 'track/stats.html', context)


@login_required(login_url='/login')
def tables(request):
    context = {'empty': True}
    qset = Solve.objects.filter(user=request.user)

    if len(qset) > 0:
        context['empty'] = False

    table = SolveTable(qset, order_by='-date')
    RequestConfig(request).configure(table)
    context['table'] = table
    return render(request, 'track/tables.html', context)


@login_required(login_url='/login')
def remove_solve(request, uuid):
    if uuid is None:
        return redirect('/track/tables')

    entry = Solve.objects.get(id=uuid)
    if entry.user == request.user:
        entry.delete()
    return redirect('/track/tables')


@login_required(login_url='/login')
def charts(request):
    context = {'empty': True}
    # qset = Solve.objects.all(user=request.user)
    # data_source = ModelDataSource(qset, fields=['date', 'centiseconds'])
    # chart = gchart.LineChart(
    #     data_source,
    #     html_id='chart_div',
    #     height=600,
    #     width=1100,
    #     options={'title': 'Solving speed over time'},
    # )

    data = [
       ['Date', 'Solve time (seconds)']
    ]
    qset = Solve.objects.filter(user=request.user)

    if len(qset) > 0:
        context['empty'] = False

    for q in qset:
        data.append([q.date, q.centiseconds / 100])
    data_source = SimpleDataSource(data=data)
    chart = gchart.LineChart(data_source,
                            height=600,
                            width=1100,
                            options={'title': 'Solving speed over time'})
    context['chart'] = chart
    return render(request, 'track/charts.html', context)
