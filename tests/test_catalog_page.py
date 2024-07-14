from pages.smartphones_page import SmartphonesPage
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page(browser):
    browser.get(browser.url + '/en-gb/catalog/smartphone')
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SmartphonesPage.PRODUCT_BANNER))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(SmartphonesPage.PAGES_COUNTER))
    WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(SmartphonesPage.PRODUCTS))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SmartphonesPage.SORT_DROPDOWN))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(SmartphonesPage.CATEGORIES_LIST))


def test_change_currency(browser):
    browser.get(browser.url + '/en-gb/catalog/smartphone')
    convert = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.CONVERT_CURRENCY))
    convert.click()
    convert_dropdown = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.CHANGE_CURRENCY))
    convert_dropdown.click()
    good_currency = WebDriverWait(browser, 1).until(EC.presence_of_all_elements_located(MainPage.CURRENT_CURRENCY))
    assert "£" in good_currency[0].text
