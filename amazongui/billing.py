from amazongui import settings
from amazongui.ui.billing import Ui_Billing
from PySide6 import QtWidgets
import logging


class BillingDialog(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()

        logging.info("Creating the billing dialog")
        self.ui = Ui_Billing()
        self.ui.setupUi(self)

        def save() -> None:
            logging.info("Saving the billing data")
            settings.card_number = self.ui.cardLine.text()
            settings.card_name = self.ui.nameLine.text()
            settings.card_month = self.ui.monthBox.currentText()
            settings.card_year = self.ui.yearBox.currentText()
            settings.card_default = self.ui.defaultCardBox.isChecked()
            settings.save()

        self.ui.buttonBox.accepted.connect(save)

        logging.info("Loading the billing data")
        self.ui.cardLine.setText(settings.card_number)
        self.ui.nameLine.setText(settings.card_name)
        self.ui.monthBox.setCurrentText(settings.card_month)
        self.ui.yearBox.setCurrentText(settings.card_year)
        self.ui.defaultCardBox.setChecked(settings.card_default)
