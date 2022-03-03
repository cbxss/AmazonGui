from amazongui.ui.list import Ui_List
from PySide6 import QtWidgets
import logging


class ListDialog(QtWidgets.QDialog):
    def __init__(self, file: str) -> None:
        super().__init__()

        logging.info("Creating the list dialog")
        self.ui = Ui_List()
        self.ui.setupUi(self)

        def save() -> None:
            logging.info("Saving accounts.txt")
            with open(file, "w") as f:
                f.write(self.ui.plainTextEdit.toPlainText())

        self.ui.buttonBox.accepted.connect(save)

        logging.info("Loading accounts.txt")
        with open(file, "r") as f:
            self.ui.plainTextEdit.setPlainText(f.read())
