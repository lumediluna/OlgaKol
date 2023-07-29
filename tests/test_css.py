from pages.elements_page import ElementsPage

def test_flex_menu(browser):
    tfm=ElementsPage(browser)
    tfm.visit()
    assert tfm.div_row.check_css('flex', '0 0 25%')
    assert tfm.div_row.check_css('max-width', '25%')
    browser.set_window_size(767,1000)
    assert tfm.div_row.check_css('flex', '0 0 100%')
    assert tfm.div_row.check_css('max-width', '100%')
    browser.set_window_size(1000,1000)