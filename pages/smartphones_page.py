from selenium.webdriver.common.by import By


class SmartphonesPage:
    CATEGORIES_LIST = (By.CSS_SELECTOR, '.list-group')
    PRODUCTS = (By.CSS_SELECTOR, '#product-list')
    SORT_DROPDOWN = (By.ID, 'input-sort')
    PRODUCT_BANNER = (By.CSS_SELECTOR, '#carousel-banner-0')
    PAGES_COUNTER = (By.CSS_SELECTOR, '.col-sm-6.text-end')
