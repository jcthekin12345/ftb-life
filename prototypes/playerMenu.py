
from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.screen import Screen
from textual.widgets import Static


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
            Horizontal
        )
