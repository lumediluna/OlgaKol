import time
import pytest
from pages.demoqa import Demoqa
from pages.accordion import Accordion
from pages.alert import Alert
from pages.browser_tab import Browser_tab
@pytest.mark.parametrize('pages',[Accordion, Alert, Demoqa, Browser_tab])
def test_seo_meta(browser,pages):
    page=pages(browser)
    page.visit()
    time.sleep(2)

    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == 'viewport'
    assert page.metaView.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
