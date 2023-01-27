from django.db import models
from main.staticdata import ModelChoices, SUBJECTS, TIME_SCHEDULE


class Teacher(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    patronymic = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to='teachers/', null=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{0} {1}.{2}.".format(self.surname, self.firstname[0], self.patronymic[0])


class Faculty(models.Model):
    name = models.CharField(max_length=200, null=True)
    short_name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "{0}".format(self.slug)

    def __str__(self):
        return "{0}, {1}".format(self.name, self.short_name)


class Building(models.Model):
    address = models.CharField(max_length=200, null=True)
    enclosure = models.IntegerField(null=True)

    def __str__(self):
        return "{0}, {1}".format(self.address, self.enclosure)


class Group(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'{self.speciality.short_name}-{self.year[-2:]}'


class Place(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    num_auditory = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.building}, кб.{self.floor}, ауд.{self.num_auditory}'


class Pair(models.Model):
    lesson = models.TextField(choices=SUBJECTS.make())
    time = models.TextField(choices=TIME_SCHEDULE.make())
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    LESSON_TYPE = ModelChoices()
    LESSON = LESSON_TYPE.add('lesson', 'Лекция')
    PRAC = LESSON_TYPE.add('prac', 'Практика')
    LAB = LESSON_TYPE.add('lab', 'Лабораторная')
    lesson_type = models.TextField(choices=LESSON_TYPE.make())

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    day = models.DateField()

    def __str__(self):
        return f'Schedule #{self.pk}'
