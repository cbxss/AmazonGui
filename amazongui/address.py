from amazongui import settings
from amazongui.ui.address import Ui_Address
from PySide6 import QtWidgets
import logging


class AddressDialog(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()

        logging.info("Creating the address dialog")
        self.ui = Ui_Address()
        self.ui.setupUi(self)

        def save() -> None:
            logging.info("Saving the address data")
            settings.country = self.ui.countryLine.text()
            settings.full_name = self.ui.nameLine.text()
            settings.phone_number = self.ui.phoneLine.text()
            settings.address_1 = self.ui.addressLine1.text()
            settings.address_2 = self.ui.addressLine2.text()
            settings.city = self.ui.cityLine.text()
            settings.state = self.ui.stateBox.currentText()
            settings.zip_code = self.ui.zipLine.text()
            settings.default = self.ui.defaultBox.isChecked()
            settings.save()

        self.ui.buttonBox.accepted.connect(save)

        logging.info("Loading the address data")
        self.ui.countryLine.setText(settings.country)
        self.ui.nameLine.setText(settings.full_name)
        self.ui.phoneLine.setText(settings.phone_number)
        self.ui.addressLine1.setText(settings.address_1)
        self.ui.addressLine2.setText(settings.address_2)
        self.ui.cityLine.setText(settings.city)
        self.ui.stateBox.setCurrentText(settings.state)
        self.ui.zipLine.setText(settings.zip_code)
        self.ui.defaultBox.setChecked(settings.default)
