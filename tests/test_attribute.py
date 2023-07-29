from pages.text_box import TextBox

def test_placeholder(browser):
    tb=TextBox(browser)
    tb.visit()
    assert tb.full_name.get_dom_attribute('placeholder') == 'Full Name'# если убрать сравнение, то просто проверим наличие
