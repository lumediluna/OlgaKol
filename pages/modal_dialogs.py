from pages.base_page import BasePage
from components.components import WebElement

class Modal_dialogs(BasePage):
    def __init__(self,driver):
        self.base_url='https://demoqa.com/modal-dialogs'

        super().__init__(driver, self.base_url)
        self.btn=WebElement(driver, 'item-3 > span')
        self.icon=WebElement(driver, '#app > header > a')