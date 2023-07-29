from pages.text_box import TextBox
import time


def test_clear(browser):
    tc=TextBox(browser)
    tc.visit()
    tc.full_name.send_keys('Koshatinka')
    time.sleep(2)
    tc.full_name.clear()
    time.sleep(2)
    assert tc.full_name.get_text()==''