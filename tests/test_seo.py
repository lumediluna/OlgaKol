import time
import pytest
from pages.demoqa import Demoqa
from pages.accordion import Accordion
from pages.alert import Alert
from pages.browser_tab import Browser_tab

def test_seo(browser):
    tt=Demoqa(browser)
    tt.visit()
    assert tt.get_title=='DEMOQA'

@pytest.mark.parametrize('pages',[Accordion, Alert, Demoqa, Browser_tab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'