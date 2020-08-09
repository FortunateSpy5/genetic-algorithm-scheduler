class Schedule:
    def __init__(self, classes_per_day):
        self.classes_per_day = classes_per_day
        self.time_per_class = None
        self.departments = []
        self.classes = []

class Department:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses


class Course:
    def __init__(self, name, teachers):
        self.name = name
        self.teacher = teachers

class Class:
    def __init__(self, course, day, slot):
        self.course = course
        self.day = day
        self.slot = slot


class Teacher:
    def __init__(self, name):
        self.name = name


class Info:
    def __init__(self):
        self.data = {}


class Population:
    pass


class GeneticAlgorithm:
    pass
