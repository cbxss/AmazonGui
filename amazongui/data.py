from dataclasses import dataclass
import logging, pickle


@dataclass
class Data:
    # Settings
    headless: bool = False
    show_images: bool = False
    use_proxies: bool = False

    # Billing
    card_number: str = ""
    card_name: str = ""
    card_month: str = "01"
    card_year: str = "2022"
    card_default : bool = False

    # Address
    country: str = "United States"
    full_name: str = ""
    phone_number: str = ""
    address_1: str = ""
    address_2: str = ""
    city: str = ""
    state: str = ""
    zip_code: str = ""
    default: bool = False

    def load(self) -> "Data":
        logging.info("Loading data class")
        try:
            self = pickle.load(open(f"data/pkl/data.pkl", "rb"))
            return self  # Hack for __init__.py
        except FileNotFoundError:
            logging.info("No data file found, using defaults")
            return Data()

    def save(self) -> None:
        logging.info("Saving data class")
        pickle.dump(self, open(f"data/pkl/data.pkl", "wb"))
