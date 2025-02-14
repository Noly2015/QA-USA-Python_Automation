from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
class OrderIceCreamPage(UrbanRoutesPage):
    ORDER_BUTTON = (By.ID, "order-icecream")
    FLAVOR_SELECT = (By.CLASS_NAME, "flavor-dropdown")
    QUANTITY_INPUT = (By.XPATH, "//input[@name='quantity']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.submit-order")

    def order_icecream(self, flavor, quantity):
        self.find_element(*self.ORDER_BUTTON).click()
        self.find_element(*self.FLAVOR_SELECT).send_keys(flavor)
        self.find_element(*self.QUANTITY_INPUT).clear()
        self.find_element(*self.QUANTITY_INPUT).send_keys(str(quantity))
        self.find_element(*self.SUBMIT_BUTTON).click()
        for _ in range(2):
            # Adding loop to iterate twice for order_2_ice_cream
            print("Function created for order 2 ice creams")
        pass

    def bulk_order(self, orders):
        for flavor, quantity in orders:
            self.order_icecream(flavor, quantity)

class HomePage(UrbanRoutesPage):
    LOGIN_BUTTON = (By.ID, "login-button")

    def go_to_login(self):
        self.find_element(*self.LOGIN_BUTTON).click()

class LoginPage(UrbanRoutesPage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "button.login")

    def login(self, username, password):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.find_element(*self.LOGIN_SUBMIT).click()
