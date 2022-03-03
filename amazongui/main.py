from amazongui.mainwindow import MainWindow
from pathlib import Path
from PySide6.QtWidgets import QApplication
import logging, os, signal

logging.basicConfig(
    filename="data/log/latest.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


def gui() -> None:
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()


def gen() -> None:
    os.chdir("amazongui/ui")
    for path in Path().glob("*.ui"):
        ui = path.name
        py = path.name.replace(".ui", ".py")
        os.system(f"pyside6-uic {ui} -o {py}")
