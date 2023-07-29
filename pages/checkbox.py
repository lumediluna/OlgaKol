from pages.base_page import BasePage
from components.components import WebElement

class Checkbox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'

        super().__init__(driver, self.base_url)
        self.checkbox=WebElement(driver, 'span.rct-checkbox')
        self.plus=WebElement(driver, '#tree-node > div > button.rct-option.rct-option-expand-all > svg > path')