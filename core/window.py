from __future__ import annotations

from PySide6.QtWidgets import QWidget


class Window:
    def __init__(
        self,
        master: QWidget,
        title: str,
        size: tuple[int, int] | None = None,
        icon: str | None = None,
    ) -> None:
        pass

class WebView:
    def __init__(self, master: WebWindow) -> None:
        pass
    def load(self, url: str) -> None:
        pass
    def loadHtml(self, html: str) -> None:
        pass

class WebWindow:
    def __init__(
        self,
        master: QWidget,
        title: str,
        htmlCode: str | None = None,
        size: tuple[int, int] | None = None,
        icon: str | None = None,
    ) -> None:
        self.webview = WebView(self)
