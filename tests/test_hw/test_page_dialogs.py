from pages.modal_dialogs import Modal_dialogs
from pages.demoqa import Demoqa


def test_modal_elements(browser):
    tme=Modal_dialogs(browser)
    tme.visit()
    assert tme.btn.check_count_elements(5)

def test_navigation_modal(browser):
    tnm=Modal_dialogs(browser)
    tnmd=Demoqa(browser)


    tnm.visit()
    tnm.refresh()
    tnm.icon.click()
    tnm.back()
    browser.set_window_size(900,400)
    tnm.forward()
    assert tnmd.equal_url()
    assert tnmd.get_title()
    browser.set_window_size(1000,1000)