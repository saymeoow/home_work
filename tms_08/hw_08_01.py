import datetime

class Employee:
    def __init__(self, first_name=str, last_name=str, age=int, profession=str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.onboarding_time = datetime.date(2007,4,23)

    def info(self):
        return print(dict({'fullname': self.first_name+self.last_name,
                           'age': self.age,
                           'working_time': (str(2022-self.onboarding_time.year)+' years',
                                            str(12-self.onboarding_time.month)+' months',
                                            str(30-self.onboarding_time.day)+' days')}))

petr=Employee(first_name='Petr',last_name='Jess',age=22,profession='doc' )
petr.info()





