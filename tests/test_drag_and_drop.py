import time

import pytest

from pages.droppable import Droppable
from selenium.webdriver import ActionChains

def test_drag_and_drop(browser):
    dad=Droppable(browser)
    action_chains=ActionChains(browser)

    dad.visit()
#@pytest.Mark.skip для пропуска теста
    assert dad.drop.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')

    action_chains.drag_and_drop(
        dad.drag.find_element(), #element
        dad.drop.find_element() #target
    ).perform()
    time.sleep(1)

    assert dad.drop.check_css ('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(1)



    action_chains.drag_and_drop_by_offset(
        dad.drag.find_element(), #element
        -200,0 #target
        ).perform()
    time.sleep(1)
    assert dad.drop.check_css ('backgroundColor', 'rgba(70, 130, 180, 1)')



