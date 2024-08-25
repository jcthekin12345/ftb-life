from textual.screen import Screen


class FtbPlayerCreator(Screen):
    """Player creator screen"""
    def __init__(self, main_menu):
        self.ftbMain = main_menu
        SCREENS = {"ftbMainMenu", self.ftbMain}

    CSS_PATH = "playerMenu.tcss"

    TITLE = "Football Life"

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Player Creation", )
        )
