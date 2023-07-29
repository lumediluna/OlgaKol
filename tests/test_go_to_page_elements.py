from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):
    page_elements = Demoqa(browser)
    next_page = ElementsPage(browser)

    page_elements.visit()
    assert page_elements.equal_url()
    page_elements.btn_elements.click()
    assert next_page.equal_url()