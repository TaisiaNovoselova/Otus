from selenium.webdriver.common.by import By


class LoginAdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
    USER_ICON = (By.CSS_SELECTOR, '.input-group-text .fa-solid')
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
