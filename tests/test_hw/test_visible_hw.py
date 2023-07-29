import time
from pages.accordion import Accordion

def  test_visible_accordion(browser):
    tva=Accordion(browser)
    tva.visit()
    assert tva.section1Content.visible()
    tva.section1Heading.click()
    time.sleep(2)
    assert not tva.section1Content.visible()

def test_visible_accordion_default(browser):
    tvad=Accordion(browser)
    tvad.visit()
    assert not tvad.section2Content.visible()
    assert not tvad.section21Content.visible()
    assert not tvad.section3Content.visible()