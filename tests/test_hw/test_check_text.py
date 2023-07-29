from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage

def test_check (browser):
    check=Demoqa(browser)
    checks=ElementsPage(browser)


    check.visit()
    check.footer.find_element()
    assert check.footer.get_text()=='© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    check.btn_elements.click()
    assert checks.text.get_text()=='Please select an item from left to start practice.'