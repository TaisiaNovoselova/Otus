from selenium.webdriver.common.by import By


class SignupPage:
    FIRST_NAME_INPUT = (By.ID, 'input-firstname')
    LAST_NAME_INPUT = (By.ID, 'input-lastname')
    EMAIL_INPUT = (By.ID, 'input-email')
    PASSWORD_BLOCK = (By.XPATH, "//*[text()='Your Password']")
    FORM_CHECK = (By.CSS_SELECTOR, '.form-check-input')
