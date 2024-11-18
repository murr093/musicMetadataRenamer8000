from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Horizontal, Vertical
from textual import events
import os

class FileImportApp(App):

    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:

        with Vertical():
            yield Static("line",classes="line")
            with Horizontal():
                yield Static("two",classes="basecont")
                yield Static("three",classes="basecont")

        yield Header()
        yield Footer()
                    


if __name__ == "__main__":
    app = FileImportApp()
    app.run()