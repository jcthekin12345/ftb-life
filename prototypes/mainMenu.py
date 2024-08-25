
from playerMenu import *
from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Button, Label, Static


class NewGameMenu(Screen[bool]):
    """New Game menu prompt"""
    def __init__(self, question: str):
        self.question = question
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label(self.question)
        yield Button("Yes", id="yes", variant="success")
        yield Button("No", id="no")

    @on(Button.Pressed, "#yes")
    def handle_yes(self) -> None:
        self.dismiss(True)

    @on(Button.Pressed, "#no")
    def handle_no(self) -> None:
        self.dismiss(False)

class MainMenu(App):
    """Main menu class"""

    CSS_PATH = "mainMenu.tcss"

    @work
    async def on_mount(self) -> None:
        if await self.push_screen_wait(
            NewGameMenu("Do you wanna create your player?"),
        ):
            self.notify("Good Answer!")
        else:
            self.notify(":-(", severity="error")

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
        """on_button_pressed method for check events"""
        if event.button.id == "exit":
            self.exit()
        elif event.button.id == "new-game":
            self.app.push_screen("createPrompt")



if __name__ == "__main__":
    app = MainMenu()
    app.run()
