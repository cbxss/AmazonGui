from amazongui import settings
from datetime import date
from selenium.common.exceptions import (
    NoSuchElementException,
    InvalidCookieDomainException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import mintotp, pickle, random, time
import undetected_chromedriver._compat as uc


class AmazonAccount:
    def __init__(self, email: str, password: str, totp: str = None) -> None:
        self.email = email
        self.password = password
        self.totp = totp
        self.cookie_file = f"data/pkl/{email}.pkl"

    def convert_proxy(self, proxy: str) -> str:
        # address:port:user:pass -> https://user:pass@address:port
        address, port, user, password = proxy.split(":")
        return f"https://{user}:{password}@{address}:{port}".replace("\n", "")

    def get_random_proxy(self) -> str:
        with open("data/txt/proxies.txt", "r") as f:
            proxies = f.read().splitlines()
            proxy = random.choice(proxies)
            return self.convert_proxy(proxy)

    def login(self, headless: bool = False) -> uc.Chrome:
        options = uc.ChromeOptions()

        if headless:
            options.add_argument("--headless")

        # https://stackoverflow.com/a/31581387 - Disable image downloading
        if not settings.show_images:
            prefs = {"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", prefs)

        if settings.use_proxies:
            proxy = self.get_random_proxy()
            options.add_argument(f"--proxy-server={proxy}")

        # Stop blocking main thread
        options.add_experimental_option("detach", True)

        driver = uc.Chrome(options=options)
        driver.get("https://amazon.com")

        # Load cookies
        try:
            for cookie in pickle.load(open(self.cookie_file, "rb")):
                driver.add_cookie(cookie)
            driver.refresh()
        # If the cookie file doesn't exist, sign in normally
        except (FileNotFoundError, InvalidCookieDomainException):
            # Sign in
            driver.find_element(By.ID, "nav-link-accountList").click()
            driver.find_element(By.ID, "ap_email").send_keys(self.email)
            driver.find_element(By.ID, "continue").click()
            driver.find_element(By.ID, "ap_password").send_keys(self.password)
            driver.find_element(By.ID, "signInSubmit").click()

            # TOTP (2FA)
            if self.totp:
                try:
                    totp = mintotp.totp(self.totp)
                    driver.find_element(By.ID, "auth-mfa-otpcode").send_keys(totp)
                    driver.find_element(By.ID, "auth-signin-button").click()
                except NoSuchElementException:
                    pass

            # Save cookies
            cookies = driver.get_cookies()
            while not "x-main" in [cookie["name"] for cookie in cookies]:
                time.sleep(5)
            pickle.dump(cookies, open(self.cookie_file, "wb"))

        return driver

    def addCard(
        self,
        driver: uc.Chrome) -> None:
        cc_num = settings.card_number
        exp_month = settings.card_month
        exp_year = settings.card_year
        first_last = settings.full_name
        zip_code = settings.zip_code
        default = settings.card_default

        driver.get("https://www.amazon.com/cpe/yourpayments/wallet")

        # add payment method
        driver.find_element(By.XPATH, "//a[@class='a-link-normal apx-wallet-add-link']").click()
        time.sleep(5)

        # credit or debit card
        driver.find_element(By.XPATH, '//*[@id="apx-add-credit-card-action-test-id"]').click()
        time.sleep(5)

        # iframe adding card
        iframe = driver.find_element(
            By.XPATH,
            "//iframe[contains(@class,'apx-secure-iframe pmts-portal-component')]",
        )
        driver.switch_to.frame(iframe)
        card = driver.find_element(
            By.XPATH,
            "//div[@class='a-column a-span8 pmts-add-credit-card-number-input-box a-span-last']",
        )

        # card number
        card.find_element(By.NAME, "addCreditCardNumber").send_keys(str(cc_num))

        # name on card
        driver.find_element(By.NAME, "ppw-accountHolderName").send_keys(str(first_last))

        # month dropdown
        driver.find_element(
            By.XPATH,
            "//span[contains(@class, 'pmts-expiry-month pmts-portal-component')]",
        ).click()
        dropdown = driver.find_element(By.XPATH, "//ul[@class='a-nostyle a-list-link']")
        dropdown = dropdown.find_elements(By.TAG_NAME, "li")
        dropdown[int(exp_month) - 1].click()

        # year dropdown
        driver.find_element(
            By.XPATH,
            "//span[contains(@class, 'pmts-expiry-year pmts-portal-component')]",
        ).click()
        dropdown = driver.find_elements(By.XPATH, "//ul[@class='a-nostyle a-list-link']")[1]
        dropdown = dropdown.find_elements(By.TAG_NAME, "li")
        dropdown[int(exp_year) - date.today().year].click()

        # add card
        driver.find_element(By.NAME, "ppw-widgetEvent:AddCreditCardEvent").click()

        # chose billing address
        time.sleep(3)
        driver.find_element(
            By.CLASS_NAME,
            "apx-show-payment-method-details-change-billing-address-button",
        ).click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "a-section.pmts-address-list")
        driver.find_element(By.XPATH, f"//*[contains(text(), '{str(zip_code)}')]").click()
        driver.find_element(By.NAME, "ppw-widgetEvent:SelectAddressEvent").click()
        time.sleep(2)

        # default card
        if default == "1":
            driver.find_element(By.NAME, "ppw-updateEverywhereAddCreditCard").click()

        # submit
        driver.find_element(By.NAME, "ppw-widgetEvent:SavePaymentMethodDetailsEvent").click()

        driver.quit()

    def changeRecentOrderCard(self, driver: uc.Chrome, last_4: int) -> None:
        try:
            action = ActionChains(driver)
            driver.get("https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first")
            driver.find_element(By.XPATH, '//*[@id="View-or-edit-order_2"]').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="a-autoid-2-announce"]').click()
            time.sleep(2)
            el = driver.find_element(By.XPATH, f"//*[ contains (text(), 'ending in {last_4}' ) ]")
            action.move_to_element(el).click().perform()
            time.sleep(3)
        except:
            pass

        driver.quit()

    def addAddress(self, driver: uc.Chrome) -> None:
        addy = settings.address_1
        city = settings.city
        state = settings.state
        zip_code = settings.zip_code
        phone = settings.phone_number
        first_last = settings.full_name
        default = settings.default

        driver.get("https://www.amazon.com/a/addresses/add?ref=ya_address_book_add_button")
        name = driver.find_element(By.NAME, "address-ui-widgets-enterAddressFullName")
        name.clear()
        name.send_keys(first_last)

        driver.find_element(By.NAME, "address-ui-widgets-enterAddressPhoneNumber").send_keys(phone)
        driver.find_element(By.NAME, "address-ui-widgets-enterAddressLine1").send_keys(addy)
        driver.find_element(By.NAME, "address-ui-widgets-enterAddressCity").send_keys(city)

        driver.find_elements(By.CLASS_NAME, "a-button-text.a-declarative")[1].click()
        time.sleep(1)
        states_dropdown = driver.find_element(By.XPATH, "//ul[@class='a-nostyle a-list-link']")
        states_dropdown.find_element(By.XPATH, f"//*[contains(text(), '{state}')]").click()

        # postal code
        driver.find_element(By.NAME, "address-ui-widgets-enterAddressPostalCode").click()
        driver.find_element(By.NAME, "address-ui-widgets-enterAddressPostalCode").send_keys(zip_code)
        
        #default
        if default : 
            driver.find_element(By.NAME, 'address-ui-widgets-use-as-my-default' ).click()
            
        # submit
        driver.find_element(By.ID, "address-ui-widgets-form-submit-button").click()

        try:
            driver.find_element(By.XPATH, "// *[contains(text(), 'Address saved')]")
        except:
            pass

        driver.quit()

    def __repr__(self) -> str:
        return f"AmazonAccount(email={self.email}, password={self.password})"
