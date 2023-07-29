from pages.elements_page import ElementsPage
from pages.demoqa import Demoqa
def test_navigation(browser):
    dk=Demoqa(browser)
    dpk= ElementsPage(browser)

    dk.visit()
    dk.btn_elements.click()
    dk.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert dpk.equal_url()

