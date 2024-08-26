from textual import work
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.screen import Screen
from textual.widgets import Button, Label, Static, Placeholder, Footer

class PlayerCreationMenu(Screen):
    """New Game menu prompt"""
    def compose(self) -> ComposeResult:
        yield Container(
            Static("Do you wanna create a player?", classes="question"),
            Horizontal(
                Button("Yes", id="yes", variant="success"),
                Button("No", id="no", variant="error"),
                classes="buttons"
            )
        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "yes":
            self.notify("Coming soon...")
        elif event.button.id == "no":
            self.app.exit()

class OptionsMenu(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Settings Menu")
        yield Footer()

class LoadGameMenu(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Load Game Menu")
        yield Footer()

class MainMenu(App):
    """Main menu class"""

    CSS_PATH = "mainMenu.tcss"
    MODES = {
        "playerCreationMenu": PlayerCreationMenu,
        "optionsMenu": OptionsMenu,
        "loadGameMenu": LoadGameMenu,
    }

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
            self.switch_mode("playerCreationMenu")



if __name__ == "__main__":
    app = MainMenu()
    app.run()
