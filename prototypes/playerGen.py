import random
import sys

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Label, Button, Footer, Header, Static

CREATE = "New Game"

class Ftb(App[str]):

    CSS_PATH = "playerGen.tcss"

    def compose(self) -> ComposeResult:
        yield Label("Do you love Textual?")
        yield Button("Yes", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")
        yield Container(
            Static(CREATE, classes="question"),
            Horizontal(
                Button("Create New Player", variant="success"),
                Button("Exit", variant="error"),
                classes="buttons",
            ),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


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
    app = Ftb()
    reply = app.run()
    print(reply)


if __name__ == "__main__":
    main()
