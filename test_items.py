link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    
    button = len(browser.find_elements_by_css_selector("#add_to_basket_form"))
    assert button > 0, "Not found"
    