from .base_page import BasePage
from .locators import MainPageLocators
from .locators import AddPageLocators
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math

class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url) 

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()

    def test_should_product_add(self):
        button = self.browser.find_element(*AddPageLocators.ADD_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        print(product_name, message)
        assert message == product_name, f"{product_name} is not {message}"

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(product_price, basket_price)
        assert product_price == basket_price, f"{product_price} not equal {basket_price}"
        

    
