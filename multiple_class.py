# Program to illustrate the creation of multiple objects for a class 

class Games:
    def __init__(self,gname):
        self.gname = gname

    def indoor(self):
        print(f"{self.gname} Chess")

    def outdoor(self):
        print(f"{self.gname} Hockey - National Game of India")

def main():
    q = Games("Indoor Game")
    i = Games("Brainly Game")
    o = Games("Outdoor")
    q.indoor()
    i.indoor()
    o.outdoor()

if __name__ == "main":
    main()