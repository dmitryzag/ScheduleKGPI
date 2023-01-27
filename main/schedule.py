from main.models import Pair


class Schedule:
    def __init__(self):
        self.schedule = Pair.objects.all()

    def get_day(self):
        pass

    def get_week(self):
        pass

    def current_week(self):
        pass

    def pagination(self):
        pass
