from pages.one_product_page import ProductPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_one_product_page(browser):
    browser.get(browser.url + '/en-gb/product/smartphone/iphone')
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(ProductPage.WRITE_REVIEW))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductPage.ADD_TO_CART_BUTTON))
    WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(ProductPage.RELATED_PRODUCTS))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(ProductPage.DESCRIPTION_TABS))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductPage.PRODUCT_IMG))
