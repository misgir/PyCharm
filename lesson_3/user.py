class User:
    def __init__(self,neme, last_neme):
        self.neme = neme
        self.last_neme = last_neme

    def say_neme (self):
        print(self.neme)

    def say_last_neme (self):
        print(self.last_neme)

    def say_full_neme(self):
        print ("{self.neme},{self.last_neme}")