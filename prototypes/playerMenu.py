from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.screen import Screen
from textual.widgets import Button, Static


class FtbPlayerCreator(Screen):
    """Player creator screen"""
    def __init__(self, main_menu):
        self.ftbMain = main_menu
        SCREENS = {"ftbMainMenu", self.ftbMain}

    CSS_PATH = "playerMenu.tcss"

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
            self.app.push_screen(self.ftbMain)
