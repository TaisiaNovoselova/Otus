from selenium.webdriver.common.by import By


class MainPage:
    CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse')
    CAROUSEL_IMAGE = (By.CSS_SELECTOR, '#carousel-banner-0 > .carousel-inner')
    MENU = (By.XPATH, '// *[text()="Mac (1)"]')
    WISH_LIST = (By.XPATH, "//*[@title='Wish List (0)']")
    HEADER = (By.CSS_SELECTOR, '#logo .img-fluid')
    ADD_TO_CART = (By.CSS_SELECTOR, '.row-cols-1 > div:nth-of-type(2) .button-group > button:nth-of-type(1) > i')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, '[name="quantity"]')
    CONVERT_CURRENCY = (By.ID, 'form-currency')
    CHANGE_CURRENCY = (By.CSS_SELECTOR, 'ul.dropdown-menu > li:nth-of-type(2)')
    CURRENT_CURRENCY = (By.CSS_SELECTOR, '.price-new')
