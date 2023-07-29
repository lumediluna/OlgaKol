import time

from pages.alert import Alert


def test_allert(browser):
    ta = Alert(browser)
    ta.visit()
    assert not ta.alert()
    ta.alert_btn.click()
    time.sleep(2)
    assert ta.alert()
    ta.alert().accept()


def test_alert_text(browser):
    tat=Alert(browser)
    tat.visit()
    tat.alert_btn.click()
    time.sleep(2)
    assert tat.alert().text == 'You clicked a button'
    tat.alert().accept()
    assert not tat.alert()

def test_confirm(browser):
    tc=Alert(browser)
    tc.visit()
    tc.confirm_btn.click()
    time.sleep(2)
    tc.alert().dismiss()
    assert tc.confirm_result.get_text() == 'You selected Cancel'


def test_prompt(browser):
    tp=Alert(browser)
    tp.visit()
    tp.prompt_Btn.click()
    time.sleep(2)
    tp.alert().send_keys('Owl')
    tp.alert().accept()
    assert tp.prompt_result.get_text()=='You entered Owl'