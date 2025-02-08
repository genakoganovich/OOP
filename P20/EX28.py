class Data:
    def __init__(self, info):  # конструктор
        self.info = list(info)

    def __getitem__(self, i):  # перегрузка [] для извлечения элемента из Data
        return self.info[i]


class Teacher:
    def __init__(self):  # конструктор
        self.work = 0  # количество учеников

    def teach(self, info, pupil):  # обучение данными из info учеников pupil
        for i in pupil:
            i.take(info)  # учим ученика i
            self.work += 1  # количество учеников увеличилось на 1


class Pupil:
    def __init__(self):  # конструктор
        self.knowledge = []  # список полученных знаний

    def take(self, info):  # получение знания
        self.knowledge.append(info)

lesson = Data(['class', 'object', 'inheritance', 'polymorphism', 'encapsulation'])
marIvanna = Teacher()
vasy = Pupil()
pety = Pupil()
marIvanna.teach(lesson[2], [vasy, pety]) # учить обоих знанию lesson[2]
marIvanna.teach(lesson[0], [pety]) # учить pety знанию lesson[0]
print(vasy.knowledge) # вывод: ['inheritance']
print(pety.knowledge) # вывод: ['inheritance', 'class']
