from pages.form_page import FormPage
import time
from selenium.webdriver.common.keys import Keys


def test_login_form(browser):
    tlf = FormPage(browser)
    tlf.visit()
    assert not tlf.modal_dialog.exist()
    time.sleep(2)
    tlf.first_name.send_keys('Catty')
    tlf.last_name.send_keys('Katson')
    tlf.user_email.send_keys('booo@kaska.com')
    tlf.gender_radio_3.click_forse()
    tlf.user_number.send_keys('89807775544')
    tlf.hobbies.click_forse()
    tlf.current_adress.send_keys('123456, Zimbabve, Zim, Down st, 333-k, 234')
    # tlf.state.click()
    # time.sleep(2)
    # tlf.state.send_keys('NCR')
    # tlf.state.send_keys(Keys.ENTER)

    time.sleep(2)
    # tlf.city.click_forse()
    # time.sleep(2)
    # tlf.city.send_keys('Delfi')
    # time.sleep(2)
    # tlf.city.click()
    # time.sleep(2)
    tlf.btn_submit.click_forse()
    time.sleep(2)
    assert tlf.modal_dialog.exist()
    tlf.btn_close_modal.click_forse()
