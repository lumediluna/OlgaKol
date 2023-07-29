from pages.elements_page import ElementsPage

def test_find_elements(browser):
    tfl=ElementsPage(browser)
    tfl.visit()
    assert tfl.btns_first_menu.check_count_elements(9)