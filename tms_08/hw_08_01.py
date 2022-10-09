class Employee:
    def __init__(self, first_name=str, last_name=str, age=int, profession=str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.onboarding_time = 0

    def onboarding_time(self):
        if any(x < 0 for x in self.onboarding_time):
            raise ValueError('value muse be positive')


