from pages.text_box import TextBox
import time
def test_text_box(browser):
    ttb=TextBox(browser)
    ttb.visit()
    ttb.full_name.send_keys('Vik King')
    ttb.current_address.send_keys('123456, Soullife, Life st., 4-6')
    time.sleep(2)
    ttb.submit.click_forse()
    assert ttb.name.exist()
    assert ttb.current_address_next.exist()
    assert ttb.name.get_text()=='Name:Vik King'
    assert ttb.current_address_next.get_text()=='Current Address :123456, Soullife, Life st., 4-6'