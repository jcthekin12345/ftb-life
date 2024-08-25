
from playerMenu import *
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Button, Static


class MainMenu(App[str]):

    CSS_PATH = "mainMenu.tcss"

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Football Life", classes="main-menu-title"),
            Vertical(
                Button("New Game", id="new-game", variant="success"),
                Button("Load Game", id="load-game", variant="success"),
                Button("Options", id="options", variant="success"),
                Button("Exit", id="exit", variant="error"),
                classes="buttons",
            ),
            id="mainMenu",
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "exit":
            self.exit()
        elif event.button.id == "new-game":
            self.app.push_screen("ftbPlayerCreation")

def main():

    app = MainMenu()
    reply = app.run()
    print(reply)


if __name__ == "__main__":
    main()
