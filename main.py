from selenium.webdriver.chrome import webdriver

import data
import helpers
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if(is_url_reachable("https://cnt-a4ec1a6b-76f6-43e0-92e4-6d24b7adf72e.containerhub.tripleten-services.com/")):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes")

    def test_set_route(self):



    def test_select_plan(self):


    def test_fill_phone_number(self):


    def test_fill_card(self):


    def test_comment_for_driver(self):


    def test_order_blanket_and_handkerchiefs(self):



    def test_order_2_ice_creams(self):

        # Loop to add 2 ice creams
        for _ in range(2):
            # Adding loop to iterate twice for order_2_ice_cream
            print("Function created for order 2 ice creams")
        pass

    def test_car_search_model_appears(self):


    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if (is_url_reachable("https://cnt-76af24d3-85c7-43cf-a38a-59daa650316f.containerhub.tripleten-services.com")):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()