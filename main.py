import random


class Schedule:
    def __init__(self, days=5, slots_per_day=4):
        self.days = days
        self.slots_per_day = slots_per_day
        self.total_slots = self.slots_per_day * self.days
        self.time_per_class = None
        self.departments = []
        self.timetable = []

    def create_departments(self):
        self.departments.append(
            Department(
                "CSE",
                [
                    Course(
                        "PCCCS501",
                        ["Kolya"],
                        3
                    ),
                    Course(
                        "PCCCS502",
                        ["Tunga"],
                        3
                    ),
                    Course(
                        "PCCCS503",
                        ["Bhattachajee"],
                        3
                    ),
                    Course(
                        "ESC501",
                        ["Monica"],
                        3
                    ),
                    Course(
                        "PECIT501",
                        ["Saha"],
                        3
                    ),
                    Course(
                        "MCCS501",
                        "Dey",
                        2
                    ),
                    Course(
                        "MCCS502",
                        ["Ray"],
                        2
                    )
                ],
                ["A", "B"]
            )
        )

    def generate_schedule(self):
        for department in range(len(self.departments)):
            self.timetable.append([])
            classes = []
            for course in self.departments[department].courses:
                for count in range(course.class_count):
                    classes.append(Class(course))
            while len(classes) < self.total_slots:
                classes.append("Break")
            self.timetable[department] = []
            for j in range(len(self.departments[department].sections)):
                random.shuffle(classes)
                self.timetable[department].append(classes.copy())
        for department in range(len(self.departments)):
            print(f"Department: {self.departments[department].name}")
            for j in range(len(self.departments[department].sections)):
                print(f"\nSection: {self.departments[department].sections[j]}")
                c = 0
                for day in range(self.days):
                    for slot in range(self.slots_per_day):
                        if self.timetable[department][j][c] == "Break":
                            print("Break", end="\t\t")
                        else:
                            print(self.timetable[department][j][c].course.name, end="\t\t")
                        c += 1
                    print()


class Department:
    def __init__(self, name, courses, sections):
        self.name = name
        self.courses = courses
        self.sections = sections


class Course:
    def __init__(self, name, teachers, class_count):
        self.name = name
        self.teacher = teachers
        self.class_count = class_count


class Class:
    def __init__(self, course, day=0, slot=0):
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


if __name__ == '__main__':
    obj = Schedule()
    obj.create_departments()
    obj.generate_schedule()
