import imghdr

from pages import radio_button
from pages.demoqa import Demoqa
import pytest
from pages.radio_button import Radiobutton
@pytest.mark.skip
def test_decor(browser):
    test_decor=Demoqa(browser)
    test_decor.visit()
    assert test_decor.h5.check_count_elements(6)
    for i in test_decor.h5.find_elements():
        assert i.text !='' #можно через assert not ==''

#@pytest.mark.skipif(True, reason)   #условие, причина пропуска- причина нужна только для отчетности, в репорт

#@pytest.mark.skipif(True, reason=' ')
def test_radio_button(browser):
#    pytest.skip() пропуск теста внутри теста


    test_radio_button=Radiobutton(browser)
    if not test_radio_button.code_status():
    pytest.skip(reason= f'Страница {Radio.base_url} недоступна')

    test_radio_button.visit()

    test_radio_button.yes.click_forse()
    assert test_radio_button.text.get_title()== 'You have selected Yes '

    test_radio_button.impressive.click_forse()
    assert test_radio_button.text.get_text() == 'You have selected Impressive '

    assert 'disable' in test_radio_button.no.get_dom_attribute('class')

