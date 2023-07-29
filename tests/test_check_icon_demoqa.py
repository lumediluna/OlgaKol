from pages.demoqa import Demoqa

def test_exist_icon(browser):
    demoqa_page = Demoqa(browser)
    demoqa_page.visit()
    demoqa_page.icon.click()
    assert demoqa_page.icon.exist()
    assert demoqa_page.equal_url()




#    browser.get('https://demoqa.com/')
#    icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')


    # if icon is None:
    #     print('Элемент не найден')
    # else:
    #     print('Элемент найден')
