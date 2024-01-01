class car:
    def __init__(self, modelname, year) -> None:
        self.modelname = modelname
        self.year = year 

    def display(self):
        print(f"{self.modelname} and {self.year}") 

    def set_modelname(self, modelname):
        self.modelname = modelname

c1 = car("Honda", "2002")
c1.display()

c1.modelname = "Toyota"
c1.display()