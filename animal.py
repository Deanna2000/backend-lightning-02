class Animal():
    def __init__(self,species, leg_num, domesticated):
        self.species = species
        self.leg_num = leg_num
        self.domesticated = domesticated

    def say_something(self):
        if self.species == "dog":
            return "Woof"
        else:
            return "moosqueakrrrrrchirp"