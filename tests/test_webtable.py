from pages.tables import Tables
import time

def test_weblables(browser):
    tw=Tables(browser)
    tw.visit()
    assert not tw.no_rows_found.exist()
    while tw.delete.exist():
        tw.delete.click()

    time.sleep(2)
    assert tw.no_rows_found.exist()