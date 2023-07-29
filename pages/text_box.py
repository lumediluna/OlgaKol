from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):
    def __init__ (self, driver):
        self.base_url = 'https://demoqa.com/text-box'


        super().__init__(driver, self.base_url)
        self.full_name= WebElement(driver,'#userName')
        self.current_address=WebElement(driver, '#currentAddress')
        self.submit=WebElement(driver, '#submit')
        self.name=WebElement(driver,'#name')
        self.current_address_next = WebElement(driver, 'p#currentAddress')