import random


class Info:
    def __init__(self):
        self.data = {
            "institute": "RCC Institute of Information Technology",
            "department_count": 1,
            "days_per_week": 5,
            "slots_per_day": 4,
            "departments": {
                "CSE": {
                    "section_count": 2,
                    "sections": {
                        "5A": {
                            "course_count": 7,
                            "courses": {
                                "ESC-501": {
                                    "name": "Software Engineering",
                                    "teachers": ["Mrs. Monica Singh"],
                                    "class_count": 3
                                },
                                "PCC-CS-501": {
                                    "name": "Compiler Design",
                                    "teachers": ["Dr. Anup Kumar Kolya"],
                                    "class_count": 3
                                },
                                "PCC-CS-502": {
                                    "name": "Operating System",
                                    "teachers": ["Mr. Harinandan Tunga"],
                                    "class_count": 3
                                },
                                "PCC-CS-503": {
                                    "name": "Object Oriented Programming",
                                    "teachers": ["Mr. Arup Kumar Bhattacharjee"],
                                    "class_count": 3
                                },
                                "PEC-IT-501": {
                                    "name": "Theory of Computation / Computer Graphics",
                                    "teachers": ["Mr. Rajib Saha", "Sk. Mazharul Islam"],
                                    "class_count": 3
                                },
                                "MC-CS-501": {
                                    "name": "Constitution of India",
                                    "teachers": ["Dr. Sadhan Kumar Dey"],
                                    "class_count": 2
                                },
                                "HS-MC-501": {
                                    "name": "Introduction to Industrial Management",
                                    "teachers": ["Mrs. Jhuma Ray"],
                                    "class_count": 2
                                }
                            }
                        },
                        "5B": {
                            "course_count": 7,
                            "courses": {
                                "ESC-501": {
                                    "name": "Software Engineering",
                                    "teachers": ["Mrs. Monica Singh"],
                                    "class_count": 3
                                },
                                "PCC-CS-501": {
                                    "name": "Compiler Design",
                                    "teachers": ["Dr. Anup Kumar Kolya"],
                                    "class_count": 3
                                },
                                "PCC-CS-502": {
                                    "name": "Operating System",
                                    "teachers": ["Mr. Harinandan Tunga"],
                                    "class_count": 3
                                },
                                "PCC-CS-503": {
                                    "name": "Object Oriented Programming",
                                    "teachers": ["Mr. Arup Kumar Bhattacharjee"],
                                    "class_count": 3
                                },
                                "PEC-IT-501": {
                                    "name": "Theory of Computation / Computer Graphics",
                                    "teachers": ["Mr. Rajib Saha", "Sk. Mazharul Islam"],
                                    "class_count": 3
                                },
                                "MC-CS-501": {
                                    "name": "Constitution of India",
                                    "teachers": ["Dr. Sadhan Kumar Dey"],
                                    "class_count": 2
                                },
                                "HS-MC-501": {
                                    "name": "Introduction to Industrial Management",
                                    "teachers": ["Mrs. Jhuma Ray"],
                                    "class_count": 2
                                }
                            }
                        }
                    }
                }
            }
        }

    def set_info(self, data):
        if data is not None:
            self.data = data


class GeneticAlgorithm:
    def __init__(self):
        self.population = None
        self.mutate_chance = 0.01
        self.population_size = 10
        self.elite_size = 0.2

    def genetic_algorithm(self, data):
        self.population = Population(self.population_size)
        self.population.initialize_data(data)
        self.population.initialize_population()
        self.population.calculate_fitness()
        self.population.display_population()

    def initialize_population(self):
        self.population.initialize_population()

    def sort_population(self):
        self.population.sort_population()

    def display_rank(self):
        self.population.display_rank()


class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        self.Data = None
        self.rank = []

    def initialize_data(self, data):
        self.Data = Data(data["institute"])
        self.Data.initialize(data)

    def initialize_population(self):
        for i in range(self.population_size):
            new_gene = Genes()
            new_gene.initialize(self.Data)
            self.population.append(new_gene)

    def display_population(self):
        for i in range(self.population_size):
            print(f"\nIndex: {i}")
            self.population[i].display()

    def calculate_fitness(self):
        for i in range(self.population_size):
            self.population[i].calculate_conflicts()


class Genes:
    def __init__(self):
        self.teacher_schedule = None
        self.schedule = None
        self.Data = None
        self.fitness = 0
        self.conflicts = 0

    def initialize(self, data):
        self.Data = data
        self.schedule = self.Data.get_random_schedule()

    def display(self):
        self.Data.display_institute(self.schedule)
        print(f"\nConflicts: {self.conflicts}")

    def calculate_conflicts(self):
        self.conflicts = self.Data.calculate_conflicts(self.schedule)


class Data:
    def __init__(self, name):
        self.days_per_week = None
        self.slots_per_day = None
        self.total_slots = None
        self.Data_name = name
        self.data = None
        self.time_per_slot = None
        self.department_count = None
        self.departments = []

    def initialize(self, data):
        self.data = data
        self.days_per_week = self.data["days_per_week"]
        self.slots_per_day = self.data["slots_per_day"]
        self.total_slots = self.slots_per_day * self.days_per_week
        self.department_count = self.data["department_count"]
        for department_name, department_data in self.data["departments"].items():
            new_department = Department(department_name)
            new_department.initialize_department(department_data, self.total_slots)
            self.departments.append(new_department)

    def get_random_schedule(self):
        schedule = []
        for i in range(self.department_count):
            department_schedule = self.departments[i].get_random_department_schedule(self.total_slots)
            schedule.append(department_schedule)
        return schedule

    def display_institute(self, schedule):
        for i in range(self.department_count):
            self.departments[i].display_department(schedule[i], self.days_per_week, self.slots_per_day)

    def calculate_conflicts(self, schedule):
        conflicts = 0
        for i in range(self.department_count):
            conflicts += self.departments[i].calculate_conflicts(schedule[i])
        conflicts += self.calculate_teacher_conflicts(schedule)
        return conflicts
    
    def calculate_teacher_conflicts(self, schedule):
        teacher_schedule = [set() for _ in range(self.total_slots)]
        conflicts = 0
        for i in range(self.department_count):
            department = self.departments[i]
            for j in range(department.section_count):
                for k in range(self.total_slots):
                    if schedule[i][j][k].code != "Break":
                        for teacher in schedule[i][j][k].teachers:
                            if teacher in teacher_schedule[k]:
                                conflicts += 1
                            else:
                                teacher_schedule[k].add(teacher)
        return conflicts


class Department:
    def __init__(self, name):
        self.name = name
        self.section_count = None
        self.sections = []

    def initialize_department(self, data, total_slots):
        self.section_count = data["section_count"]
        for section_name, section_data in data["sections"].items():
            new_section = Section(section_name)
            new_section.initialize_section(section_data, total_slots)
            self.sections.append(new_section)

    def get_random_department_schedule(self, total_slots):
        department_schedule = []
        for i in range(self.section_count):
            section_schedule = self.sections[i].get_random_section_schedule(total_slots)
            department_schedule.append(section_schedule)
        return department_schedule

    def display_department(self, schedule, days_per_week, slots_per_day):
        print(f"Department: {self.name}")
        for i in range(self.section_count):
            self.sections[i].display_section(schedule[i], days_per_week, slots_per_day)
    
    def calculate_conflicts(self, schedule):
        conflicts = 0
        for i in range(self.section_count):
            conflicts += self.sections[i].calculate_conflicts(schedule[i])
        return conflicts


class Section:
    def __init__(self, name):
        self.total_classes = 0
        self.name = name
        self.course_count = None
        self.courses = []

    def initialize_section(self, data, total_slots):
        self.course_count = data["course_count"]
        for course_code, course_data in data["courses"].items():
            new_course = Course(course_code)
            new_course.initialize_course(course_data["name"], course_data["teachers"], course_data["class_count"])
            self.total_classes += new_course.class_count
            self.courses.append(new_course)
        if self.total_classes < total_slots:
            new_course = Course("Break")
            new_course.initialize_course(None, None, total_slots - self.total_classes)
            self.courses.append(new_course)

    def get_random_course(self):
        return random.choices(self.courses, weights=[course.class_count for course in self.courses], k=1)[0]

    def get_random_section_schedule(self, total_slots):
        section_schedule = []
        for i in range(total_slots):
            section_schedule.append(self.get_random_course())
        return section_schedule

    def display_section(self, schedule, days_per_week, slots_per_day):
        index = 0
        print(f"\nSection: {self.name}")
        for i in range(days_per_week):
            for j in range(slots_per_day):
                print(f"{schedule[index].code:<20}", end="")
                index += 1
            print()

    def calculate_conflicts(self, schedule):
        conflicts = 0
        for course in self.courses:
            conflicts += abs(schedule.count(course) - course.class_count)
        return conflicts


class Course:
    def __init__(self, code):
        self.code = code
        self.name = None
        self.teachers = None
        self.class_count = None

    def initialize_course(self, name, teachers, class_count):
        self.name = name
        self.teachers = teachers
        self.class_count = class_count


if __name__ == '__main__':
    obj = GeneticAlgorithm()
    obj.genetic_algorithm(Info().data)
