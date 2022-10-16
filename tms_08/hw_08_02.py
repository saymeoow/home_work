class Employee:
    def __init__(self, first_name=str, last_name=str, age=int, profession=str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.onboarding_time = None
        self.department = None

    @property
    def onb_time(self):
        if self.onboarding_time is None:
            self.onboarding_time = f"21.4.2019"
        return self.onboarding_time


    def info(self):
        return print(dict({'fullname': str(self.first_name)+ ' '+ str(self.last_name),
                           'age': self.age,
                           'working_time': petr.onb_time,
                           'Department': petr.department}))



class TechnicalStaff(Employee):

    @property
    def change_department(self):
        return self.department

    @change_department.setter
    def set_department(self, value):
        self.department = value


petr=TechnicalStaff()
petr=TechnicalStaff(first_name='Petr',last_name='Jess',age=22,profession='doc' )
petr.set_department = 'Hospital'
petr.info()

