from django.shortcuts import render
from django.http import HttpResponse
from main.schedule import Schedule


def spec(req, faculty):
    schedule = Schedule()
    print(schedule.pagination())
    context = {'parity': Schedule.get_current_parity()}
    return render(req, 'main.html', context)


def hello(req, spec):
    page = req.GET.get('page')
    schedule = Schedule()
    page_obj = schedule.pagination().get_page(page)
    obj_week = schedule.get_week(page)
    return render(req, 'main.html', {'page_obj': page_obj, 'obj_week': obj_week})


def main_page(req):
    context = {'parity': Schedule.get_current_parity()}
    return render(req, 'faculties.html', context)
