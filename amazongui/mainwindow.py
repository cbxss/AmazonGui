from amazongui import settings, version
from amazongui.address import AddressDialog
from amazongui.amazon import AmazonAccount
from amazongui.billing import BillingDialog
from amazongui.list import ListDialog
from amazongui.ui.main import Ui_MainWindow
from PySide6 import QtWidgets
import logging, mintotp, requests, webbrowser
import undetected_chromedriver._compat as uc


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        logging.info("Creating the main window")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        logging.info("Checking for updates")
        self.checkForUpdates()

        logging.info("Setting the menubar toggles")
        self.setMenubarToggles()

        logging.info("Connecting the menubar actions")
        self.connectMenubarActions()

        logging.info("Connecting the main buttons")
        self.connectMainButtons()

        logging.info("Loading the left layout (accounts)")
        self.loadLeftLayout()

    def checkForUpdates(self) -> None:
        response = requests.get("https://shaybox.com/amazon.txt")
        remote_version = int(response.text.strip())
        if remote_version > version:
            self.ui.statusbar.showMessage(f"Update available v{remote_version}", 0)

    def setMenubarToggles(self) -> None:
        self.ui.actionHeadless.setChecked(settings.headless)
        self.ui.actionImages.setChecked(settings.show_images)
        self.ui.actionUseProxies.setChecked(settings.use_proxies)

    def connectMenubarActions(self) -> None:
        # File
        self.ui.actionQuit.triggered.connect(self.close)

        # Edit
        def showListDialog(path: str) -> None:
            ListDialog(path).exec_()
            self.loadLeftLayout()

        self.ui.actionAccounts.triggered.connect(lambda: showListDialog("data/txt/accounts.txt"))
        self.ui.actionProxies.triggered.connect(lambda: showListDialog("data/txt/proxies.txt"))
        self.ui.actionBilling.triggered.connect(lambda: BillingDialog().exec_())
        self.ui.actionAddress.triggered.connect(lambda: AddressDialog().exec_())

        # View
        self.ui.actionHeadless.triggered.connect(lambda checked: setattr(settings, "headless", checked))
        self.ui.actionImages.triggered.connect(lambda checked: setattr(settings, "show_images", checked))
        self.ui.actionUseProxies.triggered.connect(lambda checked: setattr(settings, "use_proxies", checked))

        # Help
        # Menubar action - show about dialog
        def showAboutDialog() -> None:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("About")
            msg.setText("Created by Shayne Hartford (ShayBox) and Sebastian (cbass")
            msg.exec_()

        # Menubar action - download update
        def downloadUpdate() -> None:
            webbrowser.open("https://shay.download/Private/AmazonGUI")

        # Menubar action - open changelog
        def openChangelog() -> None:
            webbrowser.open("https://shay.download/Private/AmazonGUI/changelog.txt")

        self.ui.actionAbout.triggered.connect(showAboutDialog)
        self.ui.actionUpdate.triggered.connect(downloadUpdate)
        self.ui.actionChangelog.triggered.connect(openChangelog)

    def connectMainButtons(self) -> None:
        # Main button - login
        def loginButton(headless: bool = False) -> tuple[AmazonAccount, uc.Chrome]:
            buttonGroup = self.ui.buttonGroup
            button = buttonGroup.checkedButton()
            if button is None:
                return

            account = self.accounts[button.text()]
            driver = account.login(headless)

            return (account, driver)

        # Main button - add card
        def addCardButton() -> None:
            account, driver = loginButton(settings.headless)
            account.addCard(driver)

        # Main button - change order card
        def changeRecentButton() -> None:
            account, driver = loginButton(settings.headless)
            account.changeRecentOrderCard(driver, last_4=1111)

        # Main button - add address
        def addAddressButton() -> None:
            account, driver = loginButton(settings.headless)
            account.addAddress(driver)

        self.ui.loginButton.clicked.connect(loginButton)
        self.ui.addCardButton.clicked.connect(addCardButton)
        self.ui.changeRecentButton.clicked.connect(changeRecentButton)
        self.ui.addAddressButton.clicked.connect(addAddressButton)

    def loadLeftLayout(self) -> None:
        # Clear the layout
        while self.ui.leftLayout.count():
            child = self.ui.leftLayout.takeAt(0)
            if child.widget():
                child.widget().setParent(None)

        # Load the layout
        self.accounts = {}
        self.ui.buttonGroup = QtWidgets.QButtonGroup()
        with open("data/txt/accounts.txt", "r") as f:
            for line in f.read().splitlines():
                info = line.split(":")
                email, password = info[0], info[1]
                totp = info[2] if len(info) > 2 else None
                self.accounts[email] = AmazonAccount(email, password, totp)
                button = QtWidgets.QRadioButton(email)
                button.clicked.connect(self.loadRightLayout)
                self.ui.buttonGroup.addButton(button)
                self.ui.leftLayout.addWidget(button)
        self.ui.leftLayout.addStretch()

        # Select the first account
        buttons = self.ui.buttonGroup.buttons()
        if len(buttons) > 0:
            buttons[0].click()

    def loadRightLayout(self) -> None:
        buttonGroup = self.ui.buttonGroup
        button = buttonGroup.checkedButton()
        if button is None:
            return

        account = self.accounts[button.text()]
        self.ui.email.setText(account.email)
        self.ui.password.setText(account.password)
        if account.totp:
            totp = mintotp.totp(account.totp)
            self.ui.totp.setText(totp)
        else:
            self.ui.totp.setText("N/A")
