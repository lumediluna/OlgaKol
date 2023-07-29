import time

from pages.browser_tab import Browser_tab

def test_browser_tab(browser):
    tbt=Browser_tab(browser)
    tbt.visit()
    assert len(browser.window_handles) == 1
    tbt.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)



