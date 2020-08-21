from builtins import print

from pyknow import *

LowSugar = ['shakiness', 'hunger', 'sweating', 'headache', 'pale']

HighSugar = ['thirst', 'blurred vision', 'headache', 'dry mouth', 'smelling breath', 'shortness of breath']

bool_low = [0]
bool_high = [0]

def if_lowsugar(lowsugar,s1, s2, s3, s4, s5):
    if bool_low[0] == 1:
        return False

    counter = 0
    temp_vals = []
    ss = set([s1, s2, s3, s4, s5])
    ss = list(ss)
    if len(ss) < 3:
        return False
    for x in ss:
        if x in lowsugar:
            counter += 1
    if counter > 2:
        bool_low[0] = 1
        return True
    else:
        return False


def if_highsugar(highsugar, s1, s2, s3, s4, s5, s6):
    if bool_high[0] == 1:
        return False
    counter = 0
    ss = set([s1, s2, s3, s4, s5, s6])
    ss = list(ss)
    if len(ss) < 3:
        return False
    for x in ss:
        if x in highsugar:
            counter += 1
    if counter > 2:
        bool_high[0] = 1
        return True
    else:
        return False


class Medical(KnowledgeEngine):

    @Rule(Fact(age='child'), Fact(MATCH.s1), Fact(MATCH.s2), Fact(MATCH.s3), Fact(MATCH.s4), Fact(MATCH.s5),
          TEST(lambda s1, s2, s3, s4, s5: if_lowsugar(LowSugar, s1, s2, s3, s4, s5)))
    def set_lowsugar(self):
        self.declare(Fact(lowsugar="true"))

    @Rule(Fact(age="child"), Fact(MATCH.s1), Fact(MATCH.s2), Fact(MATCH.s3), Fact(MATCH.s4), Fact(MATCH.s5),
          Fact(MATCH.s6),
          TEST(lambda s1, s2, s3, s4, s5, s6: if_highsugar(HighSugar, s1, s2, s3, s4, s5, s6)))
    def set_highsugar(self):
        self.declare(Fact(highsugar="true"))

    @Rule(Fact(lowsugar="true"), Fact(diabetic_parent="true"))
    def set_diabetic(self):
        self.declare(Fact(diabetic="true"))

    @Rule(AND(Fact('runny nose'), Fact('harsh cough')))
    def set_cold(self):
        self.declare(Fact(cold="true"))

    @Rule(AND(Fact(age="child"), Fact(cold="true"), Fact('brownish-pink rash'),
              Fact('high and fast temperature'),
              Fact('bloodshot eyes'), Fact('white spots inside cheek')))
    def set_measles(self):
        self.declare(Fact(measles="true"))

    @Rule(AND(Fact(age="child"), Fact('moderate temperature'), Fact('saliva is not normal'),
              Fact('swollen lymph nodes in neck'), Fact('dry mouth')))
    def set_mumps(self):
        self.declare(Fact(mumps="true"))

    @Rule(AND(Fact(age="child"), Fact(cold="true"), Fact('conjunctives'), Fact('strong body aches'),
              Fact('weakness'), Fact('vomiting'), Fact('sore throat'), Fact('sneezing')))
    def set_childflu(self):
        self.declare(Fact(child_flu="true"))

    @Rule(AND(Fact(age="adult"), Fact(cold="true"), Fact('conjunctives'), Fact('strong body aches'),
              Fact('weakness'), Fact('vomiting'), Fact('sore throat')), Fact('sneezing'))
    def set_adultflu(self):
        self.declare(Fact(adult_flu="true"))

    @Rule(Fact(lowsugar="true"))
    def print_lowsugar(self):
        print("You have signs of low sugar.")

    @Rule(Fact(highsugar="true"))
    def print_highsugar(self):
        print("You have signs of high sugar.")

    @Rule(Fact(diabetic="true"))
    def print_diabetic(self):
        print("You could be diabetic.")

    @Rule(Fact(cold="true"))
    def print_cold(self):
        print("You have signs of cold.")

    @Rule(Fact(measles="true"))
    def print_measles(self):
        print("You have measles.")

    @Rule(Fact(mumps="true"))
    def print_mumps(self):
        print("You have mumps.")

    @Rule(Fact(child_flu="true"))
    def print_childflu(self):
        print("You have child flu.")

    @Rule(Fact(adult_flu="true"))
    def print_adultflu(self):
        print("You have adult flu.")


def medical_expert():
    engine = Medical()
    engine.reset()
    age = int(input("Enter Your Age : "))
    if age <= 5:
        engine.declare(Fact(age="child"))
    else:
        engine.declare(Fact(age="adult"))

    while True:
        engine.declare(Fact(input("Enter a symptom: ")))
        answer = input("Do you have another symptom?(Y/N)").lower()
        if answer == "n":
            break

    dp = input("Do you have a diabetic parent?(Y/N)").lower()
    if dp == 'n':
        engine.declare(Fact(diabetic_parent="false"))
    else:
        engine.declare(Fact(diabetic_parent="true"))
    engine.run()


class Plant(KnowledgeEngine):
    b = 0
    @Rule(Fact(Temperature='high'), Fact(Humidity='normal'), Fact(TuberColor='reddish-brown'), Fact(TuberState='spots'))
    def plant1(self):
        self.b = 1
        print("The plant has black heart\n")

    @Rule(Fact(Temperature='low'), Fact(Humidity='high'), Fact(TuberColor='normal'), Fact(TuberState='spots'))
    def plant2(self):
        self.b = 1
        print("The plant has late blight\n")

    @Rule(Fact(Temperature='high'), Fact(Humidity='normal'), Fact(TuberColor='dry'), Fact(TuberState='circle'))
    def plant3(self):
        self.b = 1
        print("The plant has dry rot\n")

    @Rule(Fact(Temperature='normal'), Fact(Humidity='normal'), Fact(TuberColor='brown'), Fact(TuberState='wrinkles'))
    def plant4(self):
        self.b = 1
        print("The plant has early blight\n")


def plant_diagnosis():
    engine = Plant()
    engine.reset()
    while engine.b != 1:
        input1 = input("Is the plant Temperature High, Low or Normal?\n")
        input2 = input("Is the plant Humidity High or Normal?\n")
        input3 = input("Is the plant Tuber Color Reddish-Brown, Normal, Dry or Brown?\n")
        input4 = input("Does the plant Tuber has Spots, Circles or Wrinkles?\n")
        engine.declare(Fact(Temperature=input1.lower()))
        engine.declare(Fact(Humidity=input2.lower()))
        engine.declare(Fact(TuberColor=input3.lower()))
        engine.declare(Fact(TuberState=input4.lower()))
        engine.run()
        if engine.b == 1:
            engine.b = 0
            break
        else :
            print("Please Re-Enter the Diagnoses again.")

def main():
    f = False
    while f is False:
        print("(1) for Medical Expert System.")
        print("(2) for Plant Diagnosis Expert System.")
        choice = int(input("Your choice: "))
        if choice == 1:
            medical_expert()
            f = True
        elif choice == 2:
            plant_diagnosis()
            f = True
        else:
            print("Please re-enter your choice again.")

main()