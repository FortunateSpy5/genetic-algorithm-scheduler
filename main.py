import random


class Info:
    """
    This Class shows the structure of the information that is needed to generate the schedule. All the information needs to be valid.

    data: The institute data in proper format.
    """

    def __init__(self):
        self.data = {
            "institute": "RCC Institute of Information Technology",
            "department_count": 2,
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
                },
                "ECE": {
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
        """
        Call this function to overwrite default data.
        :param data: Information in proper format as shown in default value for data.
        :return: None
        """

        if data is not None:
            self.data = data


class GeneticAlgorithm:
    """
    GeneticAlgorithm class is used to execute the genetic algorithm.

    population: Population object, which represents the elements of current generation.
    mutate_change: The probability of mutation of each gene (each class of the schedule).
    population_size: The size of each generation population.
    elite_size: The fraction of total population that will be passed to next generation without crossover or mutation.
    max_generation: Generation at which program will be stopped if optimal output has not yet been reached.
    current_generation: Store value of current generation.
    """

    def __init__(self):
        self.population = None
        self.mutate_chance = 0.03
        self.population_size = 500
        self.elite_size = 0.25
        self.max_generation = None
        self.current_generation = 0

    def genetic_algorithm(self, data, display):
        """
        :param data: Object of class Info.
        :param display: Boolean whether to display final schedule.
        :return: Final schedule in proper format. (not yet implemented)
        """

        self.population = Population(self.population_size)
        self.population.initialize_data(data)
        self.population.initialize_population()
        self.population.calculate_fitness()
        self.population.sort_population()
        self.current_generation += 1
        while True:
            self.population.new_generation(self.elite_size, self.mutate_chance)
            self.population.calculate_fitness()
            self.population.sort_population()
            if self.population.population[self.population.rank[0]].conflicts == 0:
                if display:
                    self.population.display_generation(self.current_generation)
                break
            self.current_generation += 1
        return None


class Population:
    """
    Population class contains all the functions required for the genetic algorithm and executes them when called from GeneticAlgorithm class.

    population_size: The size of each generation population.
    population: List of genes (schedules) with the size of list being population_size.
    new_population: Used to create and store the population of next generation which then replaces current population.
    Data: Object of class Data, containing all university data.
    rank: List depicting the rank of each gene sorted in descending order of fitness.
    population_fitness: List of fitness of each gene.
    """

    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        self.new_population = []
        self.Data = None
        self.rank = []
        self.population_fitness = []

    def initialize_data(self, data):
        """
        Converts the institute information to Data object.
        :param data: Dictionary from Info object.
        :return: None
        """
        self.Data = Data(data["institute"])
        self.Data.initialize(data)

    def initialize_population(self):
        """
        Creates initial genes for Generation 0.
        :return: None
        """
        self.rank = list(range(self.population_size))
        for i in range(self.population_size):
            new_gene = Genes()
            new_gene.initialize(self.Data)
            self.population.append(new_gene)

    def display_generation(self, generation):
        """
        Displays current generation.
        :param generation: Current generation number.
        :return: None
        """
        print(f"\n\nGeneration: {generation}\nMaximum Fitness: {self.population[self.rank[0]].fitness}\nConflicts: {self.population[self.rank[0]].conflicts}")
        self.population[self.rank[0]].display()

    def calculate_fitness(self):
        """
        Calculate total conflict and fitness of the genes of current generation.
        :return: None
        """
        sum_conflict = 0
        for i in range(self.population_size):
            self.population[i].calculate_conflicts()
            sum_conflict += self.population[i].conflicts
        for i in range(self.population_size):
            self.population[i].calculate_fitness(sum_conflict)
        self.population_fitness = [i.fitness for i in self.population]

    def sort_population(self):
        """
        Sorts population of current generation in decreasing order of fitness.
        :return: None
        """
        self.rank.sort(key=lambda x: self.population_fitness[x], reverse=True)

    def new_generation(self, elite_size, mutate_chance):
        """
        Creates new population for next generation from current generation population and mutates them.
        :param elite_size: The fraction of total population that will be passed to next generation without crossover or mutation.
        :param mutate_chance: The probability of mutation of each gene (each class of the schedule).
        :return: None
        """
        elite_size *= self.population_size
        index = 0
        while index < elite_size:
            self.new_population.append(self.population[self.rank[index]])
            index += 1
        while index < self.population_size:
            self.new_population.append(self.crossover(mutate_chance))
            index += 1
        self.population = self.new_population
        self.new_population = []

    def crossover(self, mutate_chance):
        """
        Selects two genes are random (higher fitness means higher probability of getting selected for crossover)
        :param mutate_chance: The probability of mutation of each gene (each class of the schedule).
        :return: Gene object.
        """
        gene_a = random.choices(self.population, weights=self.population_fitness, k=1)[0]
        gene_b = random.choices(self.population, weights=self.population_fitness, k=1)[0]
        while gene_b == gene_a:
            gene_b = random.choices(self.population, weights=self.population_fitness, k=1)[0]

        split = random.randint(1, gene_a.Data.total_slots - 2)
        new_gene = Genes()
        new_gene.gene_crossover(gene_a, gene_b, split, mutate_chance)
        return new_gene


class Genes:
    """
    Each Gene object is a unit of population list. Gene class contains all method needed to create and manipulate the genes.

    schedule: Contains the schedule in a multidimensional list of Course objects.
    Data: Object of class Data containing all university data.
    fitness: Stores fitness of the schedule.
    conflicts: Stores total no. of conflicts of the schedule.
    """

    def __init__(self):
        self.schedule = None
        self.Data = None
        self.fitness = 0
        self.conflicts = 0

    def initialize(self, data):
        """
        Initializes the schedule.
        :param data: Object of class Data containing all university data.
        :return:None
        """
        self.Data = data
        self.schedule = self.Data.get_random_schedule()

    def display(self):
        """
        Displays schedule.
        :return: None
        """
        self.Data.display_institute(self.schedule)

    def calculate_conflicts(self):
        """
        Calculate total no. of conflicts.
        :return: None
        """
        self.conflicts = self.Data.calculate_conflicts(self.schedule)

    def calculate_fitness(self, sum_conflicts):
        """
        Calculate fitness of schedule.
        :param sum_conflicts: Sum of conflicts of all schedules of current generation.
        :return: None
        """
        self.fitness = sum_conflicts / (self.conflicts ** 2 + 1)

    def gene_crossover(self, gene_a, gene_b, split, mutate_chance):
        """
        Create new schedule by crossover of two schedules.
        :param gene_a: One of the parent genes.
        :param gene_b: One of the parent genes.
        :param split: Random split point. New schedule gets the classes from first gene till split index and the rest classes from second gene.
        :param mutate_chance: The probability of mutation of each gene (each class of the schedule).
        :return: None
        """
        self.Data = gene_a.Data
        self.schedule = self.Data.get_crossover_schedule(gene_a.schedule, gene_b.schedule, split, mutate_chance)


class Data:
    """
    Data class stores all the institute data in object format and contains methods necessary for genetic algorithm.

    days_per_week: How many days of classes are there in a week.
    slots_per_days: How many slots of classes are there in a day.
    total_slots: Total slots per week.
    institute_name: Name of the institute.
    data: Dictionary from Info object.
    time_per_slot: Duration of each slot of class.
    department_count: No. of departments in the institute.
    departments: List of Department objects.
    """

    def __init__(self, name):
        self.days_per_week = None
        self.slots_per_day = None
        self.total_slots = None
        self.institute_name = name
        self.data = None
        self.time_per_slot = None
        self.department_count = None
        self.departments = []

    def initialize(self, data):
        """
        Initializes the data of the whole institute (all the departments one by one).
        :param data: Object of class Data, containing all university data.
        :return: None
        """
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
        """
        Generates random schedule of all the departments.
        :return: Randomly generated schedule.
        """
        schedule = []
        for i in range(self.department_count):
            department_schedule = self.departments[i].get_random_department_schedule(self.total_slots)
            schedule.append(department_schedule)
        return schedule

    def display_institute(self, schedule):
        """
        Displays the schedule of all the departments.
        :param schedule: Institute schedule.
        :return: None
        """
        for i in range(self.department_count):
            self.departments[i].display_department(schedule[i], self.days_per_week, self.slots_per_day)

    def calculate_conflicts(self, schedule):
        """
        Calculates the total no. of conflicts for the entire schedule.
        :param schedule: Institute schedule.
        :return: Total no. of conflicts.
        """
        conflicts = 0
        for i in range(self.department_count):
            conflicts += self.departments[i].calculate_conflicts(schedule[i])
        conflicts += self.calculate_teacher_conflicts(schedule)
        return conflicts
    
    def calculate_teacher_conflicts(self, schedule):
        """
        Calculates the total no. of conflicts in the schedules of teachers. (Eg. Same teacher taking two different classes simultaneously.)
        :param schedule: Institute schedule.
        :return: Total no. of teacher conflicts.
        """
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

    def get_crossover_schedule(self, gene_a, gene_b, split, mutate_chance):
        """
        Create new schedule by crossover of two schedules.
        :param gene_a: One of the parent genes.
        :param gene_b: One of the parent genes.
        :param split: Random split point. New schedule gets the classes from first gene till split index and the rest classes from second gene.
        :param mutate_chance: The probability of mutation of each gene (each class of the schedule).
        :return: None
        """
        schedule = []
        for i in range(self.department_count):
            department_schedule = self.departments[i].get_crossover_department_schedule(self.total_slots, gene_a[i], gene_b[i], split, mutate_chance)
            schedule.append(department_schedule)
        return schedule


class Department:
    """
    Department class stores the data of a particular department as an object.

    name: Name of the department.
    section_count: No. of sections in the department.
    sections: List of Section objects.
    """

    def __init__(self, name):
        self.name = name
        self.section_count = None
        self.sections = []

    def initialize_department(self, data, total_slots):
        """
        Initialize the data of the particular department.
        :param data: Data of the particular department.
        :param total_slots: Total slots per week.
        :return: None
        """
        self.section_count = data["section_count"]
        for section_name, section_data in data["sections"].items():
            new_section = Section(section_name)
            new_section.initialize_section(section_data, total_slots)
            self.sections.append(new_section)

    def get_random_department_schedule(self, total_slots):
        """
        Generate random schedule for the particular department.
        :param total_slots: Total slots per week.
        :return: Random schedule for the particular department.
        """
        department_schedule = []
        for i in range(self.section_count):
            section_schedule = self.sections[i].get_random_section_schedule(total_slots)
            department_schedule.append(section_schedule)
        return department_schedule

    def display_department(self, schedule, days_per_week, slots_per_day):
        """
        Displays data of department.
        :param schedule: Department schedule.
        :param days_per_week: How many days of classes are there in a week.
        :param slots_per_day: How many slots of classes are there in a day.
        :return: None
        """
        print(f"\nDepartment: {self.name}")
        for i in range(self.section_count):
            self.sections[i].display_section(schedule[i], days_per_week, slots_per_day)
    
    def calculate_conflicts(self, schedule):
        """
        Calculates class conflicts of the department.
        :param schedule: Department schedule.
        :return: No. of class conflicts.
        """
        conflicts = 0
        for i in range(self.section_count):
            conflicts += self.sections[i].calculate_conflicts(schedule[i])
        return conflicts

    def get_crossover_department_schedule(self, total_slots, gene_a, gene_b, split, mutate_chance):
        """
        Create new schedule by crossover of two schedules.
        :param total_slots: Total slots per week.
        :param gene_a: One of the parent genes. (only genes of the particular department)
        :param gene_b: One of the parent genes. (only genes of the particular department)
        :param split: Random split point. New schedule gets the classes from first gene till split index and the rest classes from second gene.
        :param mutate_chance: The probability of mutation of each gene (each class of the schedule).
        :return: New department schedule for next generation.
        """
        department_schedule = []
        for i in range(self.section_count):
            section_schedule = self.sections[i].get_crossover_section_schedule(total_slots, gene_a[i], gene_b[i], split, mutate_chance)
            department_schedule.append(section_schedule)
        return department_schedule


class Section:
    """
    Section class stores the data of a particular section as an object.

    total_classes: Total no. of classes (No. of slots in which classes are held) (Total slots - Empty slots).
    name: Name of the section.
    course_count: No. of courses for the section students.
    courses: List of Course objects.
    """

    def __init__(self, name):
        self.total_classes = 0
        self.name = name
        self.course_count = None
        self.courses = []

    def initialize_section(self, data, total_slots):
        """
        Initialize the data of the particular section.
        :param data: Data of the particular section.
        :param total_slots: Total slots per week.
        :return: None
        """
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
        """
        :return: Random course for list of courses. Choices are weighted according to the no. of classes per week for each course.
        """
        return random.choices(self.courses, weights=[course.class_count for course in self.courses], k=1)[0]

    def get_random_section_schedule(self, total_slots):
        """
        Generate random schedule for the particular section.
        :param total_slots: Total slots per week.
        :return: Random schedule for the particular section.
        """
        section_schedule = []
        for i in range(total_slots):
            section_schedule.append(self.get_random_course())
        return section_schedule

    def display_section(self, schedule, days_per_week, slots_per_day):
        """
        Displays data of section.
        :param schedule: section schedule.
        :param days_per_week: How many days of classes are there in a week.
        :param slots_per_day: How many slots of classes are there in a day.
        :return: None
        """
        index = 0
        print(f"\nSection: {self.name}")
        for i in range(days_per_week):
            for j in range(slots_per_day):
                print(f"{schedule[index].code:<20}", end="")
                index += 1
            print()

    def calculate_conflicts(self, schedule):
        """
        Calculates class conflicts of the department.
        :param schedule: Department schedule.
        :return: No. of class conflicts.
        """
        conflicts = 0
        for course in self.courses:
            conflicts += abs(schedule.count(course) - course.class_count)
        return conflicts

    def get_crossover_section_schedule(self, total_slots, gene_a, gene_b, split, mutate_chance):
        """
        Create new schedule by crossover of two schedules.
        :param total_slots: Total slots per week.
        :param gene_a: One of the parent genes. (only genes of the particular section)
        :param gene_b: One of the parent genes. (only genes of the particular section)
        :param split: Random split point. New schedule gets the classes from first gene till split index and the rest classes from second gene.
        :param mutate_chance: The probability of mutation of each gene (each class of the schedule).
        :return: New section schedule for next generation.
        """
        section_schedule = []
        for i in range(total_slots):
            if random.random() < mutate_chance:
                section_schedule.append(self.get_random_course())
            else:
                if i < split:
                    section_schedule.append(gene_a[i])
                else:
                    section_schedule.append(gene_b[i])
        return section_schedule


class Course:
    """
    Course class contains the details of each course and the objects of this class make up each unit of the genes.
    To account for the empty slots, a course with the code "Break" is added to the courses list. This object only has code and class_count. Other properties are not initialized.
    code: Course code.
    name: Course name.
    teachers: List of teachers for the course.
    class_count: Total no. of class per week for the particular course.
    """
    def __init__(self, code):
        self.code = code
        self.name = None
        self.teachers = None
        self.class_count = None

    def initialize_course(self, name, teachers, class_count):
        """
        Initializes the course details other than
        :param name: Course name.
        :param teachers: List of teachers for the course.
        :param class_count: Total no. of class per week for the particular course.
        :return: None
        """
        self.name = name
        self.teachers = teachers
        self.class_count = class_count


if __name__ == '__main__':
    display_best = True
    obj = GeneticAlgorithm()
    obj.genetic_algorithm(Info().data, display_best)
