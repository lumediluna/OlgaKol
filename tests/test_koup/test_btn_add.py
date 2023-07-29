from pages.herokuapp import Herokuapp
from pages.herokuapp_add import Herokuapp_add
def test_btn_add(browser):
    tba=Herokuapp(browser)
    tbaa=Herokuapp_add(browser)
    tba.visit()
    #assert tba.add_remove_element.exist()
    assert tba.add_remove_element.get_text()=='Add/Remove Elements'
    tba.add_remove_element.click()

    assert tbaa.equal_url()
    #assert tbaa.add_element.exist()
    assert tbaa.add_element.get_text()=='Add Element'
    assert tbaa.add_element.get_dom_attribute('onclick') == 'addElement()'

    for I in range(4):
        tbaa.add_element.click()

    assert tbaa.btn_delete.check_count_elements(4)

    for I in tbaa.btn_delete.find_elements():
        assert I.text == 'Delete'


#while tbaa.btn_delete.click():
    #tbaa.btn_delete.click()

    for I in range(4):
        tbaa.btn_delete.click()
    assert not tbaa.btn_delete.exist()
