from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_main_page(browser):
    browser.get(browser.url)
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(MainPage.CART_BUTTON))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(MainPage.CAROUSEL_IMAGE))
    WebDriverWait(browser, 2).until(EC.invisibility_of_element_located(MainPage.MENU))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(MainPage.WISH_LIST))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.HEADER))


def test_add_product_main(browser):
    browser.get(browser.url)
    btn_add_to_cart = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(MainPage.ADD_TO_CART))
    browser.execute_script("arguments[0].scrollIntoView();", btn_add_to_cart[0])
    browser.execute_script("arguments[0].click();", btn_add_to_cart[0])
    browser.execute_script("window.scrollBy(0, -1000);")
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[text()="Shopping Cart"]'))
    )
    browser.execute_script("arguments[0].click();", button)
    quantity = WebDriverWait(browser, 10).until(EC.presence_of_element_located(MainPage.PRODUCT_QUANTITY))

    quantity = quantity.get_attribute("value")
    assert quantity == "1", "В корзине более одного товара или товар отсутствует"


def test_change_currency(browser):
    browser.get(browser.url)
    convert = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.CONVERT_CURRENCY))
    convert.click()
    convert_dropdown = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.CHANGE_CURRENCY))
    convert_dropdown.click()
    good_currency = WebDriverWait(browser, 1).until(EC.presence_of_all_elements_located(MainPage.CURRENT_CURRENCY))
    assert "£" in good_currency[0].text



