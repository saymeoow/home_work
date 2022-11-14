class Employee:
    def __init__(self, first_name=str, last_name=str, age=int, profession=str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.onboarding_time = f"21.4.2019"

    def info(self):
        return {'fullname': self.first_name+' '+self.last_name,
                           'age': self.age,
                           'working_time': self.onboarding_time}

petr=Employee(first_name='Petr',last_name='Jess',age=22,profession='doc' )
print(petr.info())







