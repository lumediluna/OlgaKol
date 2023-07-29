from pages.elements_page import ElementsPage
import time
def test_visible_btn_sidebar(browser):
    visi=ElementsPage(browser)

    visi.visit()
   # vis.btn_sidebar_first.click()
    time.sleep(3)
   # assert vis.btn_sidebar_first_textbox.exist()
    assert visi.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    nvisi=ElementsPage(browser)
    nvisi.visit()
    assert nvisi.btn_sidebar_first_checkbox.visible()
    nvisi.btn_sidebar_first.click()
    time.sleep(2)
    assert not nvisi.btn_sidebar_first_checkbox.visible()