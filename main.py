import random


class Data:
    def __init__(self):
        self.data = {
            "institute": "RCC Institute of Information Technology",
            "department_count": 1,
            "departments": {
                "CSE": {
                    "section_count": 2,
                    "sections": {
                        "5A": {
                            "days_per_week": 5,
                            "slots_per_day": 4,
                            "course_count": 7,
                            "courses": {
                                "ESC-501": {
                                    "name": "Software Engineering",
                                    "teacher": ["Mrs. Monica Singh"],
                                    "class_count": 3
                                },
                                "PCC-CS-501": {
                                    "name": "Compiler Design",
                                    "teacher": ["Dr. Anup Kumar Kolya"],
                                    "class_count": 3
                                },
                                "PCC-CS-502": {
                                    "name": "Operating System",
                                    "teacher": ["Mr. Harinandan Tunga"],
                                    "class_count": 3
                                },
                                "PCC-CS-503": {
                                    "name": "Object Oriented Programming",
                                    "teacher": ["Mr. Arup Kumar Bhattacharjee"],
                                    "class_count": 3
                                },
                                "PEC-IT-501": {
                                    "name": "Theory of Computation / Computer Graphics",
                                    "teacher": ["Mr. Rajib Saha", "Sk. Mazharul Islam"],
                                    "class_count": 3
                                },
                                "MC-CS-501": {
                                    "name": "Constitution of India",
                                    "teacher": ["Dr. Sadhan Kumar Dey"],
                                    "class_count": 2
                                },
                                "HS-MC-501": {
                                    "name": "Introduction to Industrial Management",
                                    "teacher": ["Mrs. Jhuma Ray"],
                                    "class_count": 2
                                }
                            }
                        },
                        "5B": {
                            "days_per_week": 5,
                            "slots_per_day": 4,
                            "course_count": 7,
                            "courses": {
                                "ESC-501": {
                                    "name": "Software Engineering",
                                    "teacher": ["Mrs. Monica Singh"],
                                    "class_count": 3
                                },
                                "PCC-CS-501": {
                                    "name": "Compiler Design",
                                    "teacher": ["Dr. Anup Kumar Kolya"],
                                    "class_count": 3
                                },
                                "PCC-CS-502": {
                                    "name": "Operating System",
                                    "teacher": ["Mr. Harinandan Tunga"],
                                    "class_count": 3
                                },
                                "PCC-CS-503": {
                                    "name": "Object Oriented Programming",
                                    "teacher": ["Mr. Arup Kumar Bhattacharjee"],
                                    "class_count": 3
                                },
                                "PEC-IT-501": {
                                    "name": "Theory of Computation / Computer Graphics",
                                    "teacher": ["Mr. Rajib Saha", "Sk. Mazharul Islam"],
                                    "class_count": 3
                                },
                                "MC-CS-501": {
                                    "name": "Constitution of India",
                                    "teacher": ["Dr. Sadhan Kumar Dey"],
                                    "class_count": 2
                                },
                                "HS-MC-501": {
                                    "name": "Introduction to Industrial Management",
                                    "teacher": ["Mrs. Jhuma Ray"],
                                    "class_count": 2
                                }
                            }
                        }
                    }
                }
            }
        }

    def get_data(self, data):
        if data is not None:
            self.data = data


class GeneticAlgorithm:
    def __init__(self):
        self.population = None
        self.mutate_chance = 0.05
        self.population_size = 1
        self.elite_size = 0.2
        self.discard = 0.4

    def genetic_algorithm(self, data):
        self.population = Population(self.population_size)
        self.population.initialize(data)
        self.population.create_population(data)


class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.schedules = []
        self.institute = None

    def initialize(self, data):
        self.institute = Institute(data["institute"])
        self.institute.create_schedule(data)

    def create_population(self, data):
        for pop_index in range(self.population_size):
            for department in self.institute.departments:
                for section in department.sections:
                    section.schedule.append([])
                    for i in range(section.total_slots):
                        section.schedule[pop_index].append(section.get_random_course())
                    section.display_schedule(pop_index)


class Institute:
    def __init__(self, name):
        self.institute_name = name
        self.data = None
        self.time_per_slot = None
        self.department_count = None
        self.departments = []

    def create_schedule(self, data):
        self.data = data
        self.department_count = self.data["department_count"]
        for department_name, department_data in self.data["departments"].items():
            new_department = Department(department_name)
            new_department.create_department(department_data)
            self.departments.append(new_department)

    def generate_schedule(self):
        """
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

        """


class Department:
    def __init__(self, name):
        self.name = name
        self.section_count = None
        self.sections = []

    def create_department(self, data):
        self.section_count = data["section_count"]
        for section_name, section_data in data["sections"].items():
            new_section = Section(section_name)
            new_section.create_section(section_data)
            self.sections.append(new_section)


class Section:
    def __init__(self, name):
        self.total_classes = 0
        self.name = name
        self.days_per_week = None
        self.slots_per_day = None
        self.total_slots = None
        self.course_count = None
        self.courses = []
        self.schedule = []

    def create_section(self, data):
        self.days_per_week = data["days_per_week"]
        self.slots_per_day = data["slots_per_day"]
        self.total_slots = self.slots_per_day * self.days_per_week
        self.course_count = data["course_count"]
        for course_code, course_data in data["courses"].items():
            new_course = Course(course_code)
            new_course.create_course(course_data["name"], course_data["teacher"], course_data["class_count"])
            self.total_classes += new_course.class_count
            self.courses.append(new_course)
        if self.total_classes < self.total_slots:
            new_course = Course("Break")
            new_course.create_course(None, None, self.total_slots - self.total_classes)
            self.courses.append(new_course)

    def get_random_course(self):
        return random.choices(self.courses, weights=[course.class_count for course in self.courses], k=1)[0]

    def display_schedule(self, pop_index):
        index = 0
        print(f"\n{self.name}")
        for day in range(self.days_per_week):
            for slots in range(self.slots_per_day):
                print(f"{self.schedule[pop_index][index].code:<20}", end="")
                index += 1
            print()


class Course:
    def __init__(self, code):
        self.code = code
        self.name = None
        self.teacher = None
        self.class_count = None

    def create_course(self, name, teacher, class_count):
        self.name = name
        self.teacher = teacher
        self.class_count = class_count


class Class:
    def __init__(self, course, day=None, slot=None):
        self.course = course
        self.day = day
        self.slot = slot


if __name__ == '__main__':
    obj = GeneticAlgorithm()
    obj.genetic_algorithm(Data().data)
    print(1)
