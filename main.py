import random


class Info:
    def __init__(self, data=None):
        default = {
            "institute": "RCC Institute of Information Technology",
            "days_per_week": 5,
            "slots_per_day": 4,
            "time_per_slot": 45,
            "department_count": 1,
            "departments": {
                "CSE": {
                    "section_count": 2,
                    "sections": ["5A, 5B"],
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
        if data is None:
            self.data = default
        else:
            self.data = data


class Schedule:
    def __init__(self):
        self.data = Info().data()
        self.days_per_week = self.data["days_per_week"]
        self.slots_per_day = self.data["slots_per_day"]
        self.total_slots = self.slots_per_day * self.days_per_week
        self.time_per_slot = self.data["time_per_slot"]
        self.department_count = self.data["department_count"]
        self.departments = []

    def create_departments(self):
        for department_name, department_data in self.data["departments"].items():
            new_department = Department(department_name)
            new_department.section_count = department_data["section_count"]
            for section_name in department_data["sections"]:
                new_section = Section(section_name)
                new_section.create_section(department_data["courses"])
                new_department.sections.append(new_section)
            self.departments.append(new_department)
    
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
    def __init__(self, name):
        self.name = name
        self.section_count = None
        self.sections = []


class Section:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def create_section(self, courses_dict):
        pass

class Course:
    def __init__(self, name, code, teachers, class_count):
        self.name = name
        self.code = code
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


class Population:
    pass


class GeneticAlgorithm:
    pass


if __name__ == '__main__':
    obj = Schedule()
    obj.create_departments()
    obj.generate_schedule()
