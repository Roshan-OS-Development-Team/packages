import os

from PySide6.QtWidgets import QWidget

import core


class WebOrbit(core.WebWindow):
    def __init__(self, master: QWidget) -> None:
        super().__init__(
            master,
            "WebOrbit",
            size=(1200, 800),
            icon=os.path.join(__file__, "WebOrbit.png"),
        )
        self.webview.load("https://sorabora.github.io/weborbit/")
