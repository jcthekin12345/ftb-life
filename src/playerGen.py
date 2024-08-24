import random

class Player:
    def __init__(self):
        self.name: str
        self.age: int
        self.position: tuple[str]


class playerGen(Player):
    def __init__(self):
        super().__init__()


    def generate_starter(self):
        self.name = ""
