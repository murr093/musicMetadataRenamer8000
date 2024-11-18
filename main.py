from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual import events
import os

class FileImportApp(App):

    CSS_PATH = "style.tcss"


    # Creating the composition  
    def compose(self) -> ComposeResult:

        with Vertical():
            yield Static("line",classes="line") # The string
            with Horizontal(): 
                # yield Static("two",classes="modulesContainer") # Modules container 
                with VerticalScroll(id="modulesContainer"):
                    yield Static("module1",classes="module")
                    yield Static("module2",classes="module")
                    yield Static("module3",classes="module")
                yield Static("three",classes="basecont") # "Didn't decide yet" container

        yield Header()
        yield Footer()
                    

# Running stuff
if __name__ == "__main__":
    app = FileImportApp()
    app.run()