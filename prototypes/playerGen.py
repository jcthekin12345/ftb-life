import random
class Player:
    def __init__(self, **kwargs):
        self.name  = kwargs.get("name")
        self.age = kwargs.get("age")
        self.position = kwargs.get("position")

    def __str__(self):
        return f"name: {self.name} age: {self.age} positions: {self.position}"

    def createPlayer(self):
        pass


def player_gen():

    print(Player(name="Joaquin Coetzee", age=18, position=("CAM", "AMC", "AML", "AMR")))



if __name__ == "__main__":
    player_gen()
