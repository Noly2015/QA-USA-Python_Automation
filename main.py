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
        # Add in S8
        print("Function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("Function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("Function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("Function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("Function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Loop to add 2 ice creams
        for _ in range(2):
            # Add in S8
            pass
        print("Function created for order 2 ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created for car search model appears")
        pass