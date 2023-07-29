from pages.elements_page import ElementsPage
from components.components import WebElement
from pages.demoqa import Demoqa

def test_page_elements(browser):
    textelems = ElementsPage(browser)
    textelems.visit()
    assert textelems.text.get_text()=='Elements'
    assert textelems.icon.exist()
    assert textelems.btn_sidebar_first.exist()
    assert textelems.btn_sidebar_first_textbox.exist()

