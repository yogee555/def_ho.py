# home & practice
class home:
    def __init__(self,study,raiding,race):
        self.study=study
        self.raiding=raiding
        self.race=race
    def greet(self):
        print("study historical placess for tourism",self.study)
        print("raiding a horse in tourism placess",self.raiding)
        print("bike race in road with limeted speed",self.race)
yog = home("yogee","horse","bike")
yog.greet()

