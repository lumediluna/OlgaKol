from pages.base_page import BasePage
from components.components import WebElement



class Demoqa(BasePage):
    def __init__ (self, driver):
        self.base_url = 'https://demoqa.com/'


        super().__init__(driver, self.base_url)
        self.icon= WebElement(driver,'#app > header > a')
        self.btn_elements=WebElement(driver, '#app>div > div > div.home-body > div > div:nth-child(1)')
        self.footer=WebElement(driver, '#app > footer > span')
        self.h5=WebElement(driver, 'div.card-body > h5')

   # def click_on_the_icon(self):
     #   self.find_element(locator='#app > header > a').click()



 #   def click_on_the_bth_elements(self):
   #     self.find_element(locator='#app>div > div > div.home-body > div > div:nth-child(1)').click()
