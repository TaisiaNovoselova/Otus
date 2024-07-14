from pages.login_admin_page import LoginAdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_admin_page(browser):
    browser.get(browser.url + '/administration')
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(LoginAdminPage.USERNAME_INPUT))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(LoginAdminPage.PASSWORD_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(LoginAdminPage.LOGIN_BUTTON))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(LoginAdminPage.USER_ICON))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(LoginAdminPage.OPENCART_LINK))


def test_login(browser):
    browser.get(browser.url + '/administration')
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys("user")
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    user_name = browser.find_element(By.CSS_SELECTOR, '.d-lg-inline')
    assert user_name.text == "   John Doe", "При логине произошла ошибка"
    browser.find_element(By.CSS_SELECTOR, '#nav-logout').click()
    header_login_page = browser.find_element(By.CSS_SELECTOR, '.card-header')
    assert (
            header_login_page.text == "Please enter your login details."
    ), "При разлолгине произошла ошибка"
