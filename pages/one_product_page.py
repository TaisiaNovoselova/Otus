from selenium.webdriver.common.by import By


class ProductPage:
    PRODUCT_IMG = (By.CSS_SELECTOR, '.img-thumbnail.mb-3')
    WRITE_REVIEW = (By.XPATH, "//*[text()='Write a review']")
    DESCRIPTION_TABS = (By.XPATH, "//*[@data-bs-toggle='tab']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#product #button-cart')
    RELATED_PRODUCTS = (By.CSS_SELECTOR, '.row-cols-sm-2 .mb-3')
