from pages.checkbox import Checkbox

def test_count_checkbox(browser):
    tch=Checkbox(browser)
    tch.visit()
    assert tch.checkbox.check_count_elements(1)
    tch.plus.click()
    assert tch.checkbox.check_count_elements(17)

    for element in tch.checkbox.find_elements():
        assert element.is_displayed()

    browser.refresh()
    assert tch.checkbox.check_count_elements(1)

