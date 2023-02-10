from django.shortcuts import render
from main.schedule import Schedule


def main(req, faculty='', spec=''):
    schedule = Schedule()
    faculties = schedule.faculties
    specialities = schedule.specialities.filter(faculty__slug=faculty)
    groups = schedule.groups.filter(speciality__slug=spec)
    items = groups or specialities or faculties
    current_parity = Schedule.get_current_parity()

    context = {'items': items, 'parity': current_parity}

    return render(req, 'items.html', context)


def sched(req, **kwargs):
    schedule = Schedule()
    # items = schedule.groups.filter(speciality__faculty__slug=faculty, speciality__slug=spec)
    current_parity = Schedule.get_current_parity()

    context = {'items': {}, 'parity': current_parity}

    return render(req, 'schedule.html', context)
