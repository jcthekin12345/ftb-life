import random
import sys

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.screen import Screen
from textual.widgets import Label, Button, Footer, Header, Static, Input


class FtbPlayerCreator(Screen):
    """Player creator screen class"""
    CSS_PATH = "playerGen.tcss"
    TITLE = "Football Life"

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Player Creation", classes="question"),
            Horizontal(
                Button("Create New Player", id="create-player", variant="success"),
                Button("Exit", id="exit",variant="error"),
                classes="buttons",
            ),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "exit":
            self.exit()

class FtbMainMenu(App[str]):

    SCREENS = {"ftbPlayerCreation": FtbPlayerCreator}

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Football Life", classes="main-menu-title"),
            Horizontal(
                Button("New Game", id="new-game", variant="success"),
                Button("Load Game", id="load-game", variant="success"),
                Button("Options", id="options", variant="success"),
                Button("Exit", id="exit", variant="error"),
            ),
            id="dialog",
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "new-game":
            pass



class Player:
    def __init__(self, **kwargs):
        self.name  = kwargs.get("name")
        self.age = kwargs.get("age")
        self.position = kwargs.get("position")

    def __str__(self):
        return f"name: {self.name} age: {self.age} positions: {self.position}"

    def createPlayer(self):
        print("Create your player.")

def main():

    print(Player(name="Joaquin Coetzee", age=18, position=("CAM", "AMC", "AML", "AMR")))
    app = FtbMainMenu()
    reply = app.run()
    print(reply)


if __name__ == "__main__":
    main()
