import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import helpers


class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_LOCATOR = (By.CSS_SELECTOR, ".button.round")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".smart-button")

    SUPPORTIVE_CLASS = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    SUPPORTIVE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')

    PHONE_NUMBER_BUTTON = (By.CLASS_NAME, 'np-text')
    PHONE_NUMBER_INPUT = (By.ID, 'phone')
    NEXT_BUTTON_INPUT = (By.XPATH, '//button[contains(text(), "Next")]')
    SMS_CODE = (By.ID, 'code')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Confirm")]')

    PAYMENT_METHOD_LOCATOR = (By.CLASS_NAME, 'pp-text')
    ADD_CARD_LOCATOR = (By.XPATH, '//div[text()="Add card"]')
    CARD_NUMBER_LOCATOR = (By.ID, 'number')
    CVV_LOCATOR = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(),"Link")]')

    COMMENT_FIELD_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label')
    COMMENT_FOR_DRIVER = (By.XPATH, '//*[@id="comment"]')

    BLANKET_HANDKERCHIEF_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[1]')
    SLIDER_ROUND_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')

    ICE_CREAM_LOCATOR = (By.XPATH, '//div[@class="counter-plus"]')
    ICE_CREAM_COUNTER_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')

    ORDER_BUTTON_LOCATOR = (By.CLASS_NAME, 'smart-button-main')
    ORDER_DETAILS_LOCATOR = (By.CLASS_NAME, 'order-button')
    CAR_SEARCH_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[1]')

    def __init__(self, driver):
        self.driver = driver

    def input_from(self, from_address):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_address)

    def input_to(self, to_address):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_address)

    def click_call_taxi(self):
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()

    def input_addresses(self, from_address, to_address):
        self.input_from(from_address)
        self.input_to(to_address)
        self.click_call_taxi()

    def click_supportive(self):
        self.driver.find_element(*self.SUPPORTIVE_BUTTON).click()

    def enter_phone_number(self, number):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(number)
        self.driver.find_element(*self.NEXT_BUTTON_INPUT).click()
        self.driver.find_element(*self.SMS_CODE).send_keys(helpers.retrieve_phone_code(self.driver))
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def input_card_number (self, card_number, cvv_number):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()
        time.sleep(2)
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)
        self.driver.find_element(*self.CVV_LOCATOR).send_keys(cvv_number)
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def input_comment(self, comment_for_driver):
        self.driver.find_element(*self.COMMENT_FIELD_LOCATOR).click()
        self.driver.find_element(*self.COMMENT_FOR_DRIVER).send_keys(comment_for_driver)

    def order_blanket_handkerchiefs(self):
        self.driver.find_element(*self.SLIDER_ROUND_LOCATOR).click()

    def order_icecream(self):
            for _ in range(2):
                # Adding loop to iterate twice for order_2_ice_cream
                self.driver.find_element(*self.ICE_CREAM_LOCATOR).click()
            pass

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    def get_from(self):
        return self.driver.find_element (*self.FROM_LOCATOR).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property('value')

    def get_phone(self):
        return self.driver.find_element (*self.PHONE_NUMBER_INPUT).get_property('value')

    def get_supportive(self):
        return self.driver.find_element (*self.SUPPORTIVE_CLASS).get_attribute('class')

    def get_ice_cream(self):
        return self.driver.find_element (*self.ICE_CREAM_COUNTER_LOCATOR).text

    def get_car_search(self):
        return self.driver.find_element(*self.CAR_SEARCH_LOCATOR).text

    def get_card(self):
        return self.driver.find_element(*self.CARD_NUMBER_LOCATOR).get_property('value')

    def get_cvv(self):
        return self.driver.find_element(*self.CVV_LOCATOR).get_property('value')

    def get_blanket_handkerchief(self):
        return self.driver.find_element(*self.BLANKET_HANDKERCHIEF_LOCATOR).text

    def get_comment_for_driver(self):
        return self.driver.find_element(*self.COMMENT_FOR_DRIVER).get_property('value')