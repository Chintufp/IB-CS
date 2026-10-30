class course:
    def __init__(self, name:str, topic:str, nameTeach:str, numPar:int):
        self.name = name
        self.topic = topic
        self.nameTeach = nameTeach
        self.numPar = numPar

    def __str__(self):
        return f'{self.name} ({self.topic}) by {self.nameTeach}, {self.numPar} participants'

cs = course('IBCS', 'Computer Science', 'Jarmo', 30)
print(cs)