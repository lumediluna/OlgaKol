import time
from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_size(browser):
    ts=Demoqa(browser)
    ts.visit()
    browser.set_window_size(1000,300)
    time.sleep(2)
    browser.set_window_size(1000,1000)

def test_visible_nav_bar(browser):
    tvnb=ElementsPage(browser)
    tvnb.visit()
    assert not tvnb.nav_bar.visible()
    browser.set_window_size(767, 1000)
    assert tvnb.nav_bar.visible()
    browser.set_window_size(1000,1000)

