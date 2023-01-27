from collections import OrderedDict
from dataclasses import dataclass
import datetime


class ModelChoices(OrderedDict):
    def __init__(self, *a, **kw):
        super(ModelChoices, self).__init__(*a, **kw)
        self.set = list(*a) + list(kw.items())

    def add(self, key, description):
        self.set.append((key, description))
        self[key] = description
        return key

    def make(self):
        return self.set


SUBJECTS = ModelChoices()
SUBJECT_MATH = SUBJECTS.add('math', 'Математика')
SUBJECT_RUSSIAN = SUBJECTS.add('russian', 'Русский')
SUBJECT_SOCIO = SUBJECTS.add('socio', 'Социология')

TIME_SCHEDULE = ModelChoices()
TIME_FIRST = TIME_SCHEDULE.add('first_pair', '08:30 - 10:05')
TIME_SECOND = TIME_SCHEDULE.add('second_pair', '10:15 - 11:50')
TIME_THIRD = TIME_SCHEDULE.add('third_pair', '12:15 - 13:50')
TIME_FOUR = TIME_SCHEDULE.add('fourth_pair', '14:15 - 15:35')
TIME_FIVE = TIME_SCHEDULE.add('fifth_pair', '16:00 - 17:35')
