from main.models import Pair, Faculty, Speciality, Group
from django.core.paginator import Paginator
import datetime


class Schedule:
    TODAY = datetime.date.today()
    TOTAL_WEEKS = 52

    def __init__(self):
        self.schedule = Pair.objects.all()
        self.faculties = Faculty.objects.all()
        self.specialities = Speciality.objects.all()
        self.groups = Group.objects.all()

    @classmethod
    def get_current_parity(cls):
        week = cls.TODAY.isocalendar().week % 2
        word = 'НЕЧЕТНАЯ' if week else 'ЧЕТНАЯ'
        style = 'odd' if week else 'even'

        return {'style': style, 'word': word}

    def get_day(self):
        pass

    def get_week(self, num_week):
        return self.schedule.filter(day__week=num_week)

    def get_current_week(self):
        return self.schedule.filter(day__week=self.TODAY.isocalendar().week)

    def get_all_weeks(self):
        return [self.get_week(week) for week in range(1, self.TOTAL_WEEKS + 1)]

    def pagination(self):
        pages = Paginator(self.get_all_weeks(), 1)
        return pages
