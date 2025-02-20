from selenium import webdriver

import data

from pages import UrbanRoutesPage


from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        if is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from()== data.ADDRESS_FROM
        assert routes_page.get_to()== data.ADDRESS_TO

    def test_select_supportive_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_supportive()
        assert routes_page.get_supportive()== "tcard active"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        assert routes_page.get_phone()== data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.input_card_number(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.get_card()== data.CARD_NUMBER
        assert routes_page.get_cvv()== data.CARD_CODE

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.input_comment(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_comment_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_supportive()
        routes_page.order_blanket_handkerchiefs()
        assert routes_page.get_blanket_handkerchief() == "Blanket and handkerchiefs"

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_supportive()
        routes_page.order_icecream()
        assert routes_page.get_ice_cream() == "2"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_supportive()
        routes_page.input_comment(data.MESSAGE_FOR_DRIVER)
        routes_page.click_order_button()
        assert routes_page.get_car_search() == "Car search"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()