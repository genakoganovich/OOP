class Passport():
    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country = country
        self.numb_of_pasport = numb_of_pasport

    def PrintInfo(self):
        print("\nFullname: ", self.first_name, " ", self.last_name)
        print("Date of birth: ", self.date_of_birth)
        print("County: ", self.country)
        print("Passport number: ", self.numb_of_pasport)


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport, visa):
        super().__init__(first_name, last_name, country, date_of_birth, numb_of_pasport)
        self.visa = visa

    def PrintInfo(self):
        super().PrintInfo()
        print("Visa: ", self.visa)
PassportList=[]
request = ForeignPassport('Ivan', 'Ivanov', 'Russia', '12.03.1967', '123456789',
'USA')
PassportList.append(request)
request = Passport('Иван', 'Иванов', 'Россия', '12.03.1967', '45001432')
PassportList.append(request)
request = ForeignPassport('Peter', 'Smit', 'USA', '01.03.1990', '21435688',
'Germany')
PassportList.append(request)
for emp in PassportList:
    emp.PrintInfo()