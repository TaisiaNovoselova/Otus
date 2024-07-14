from pages.signup_page import SignupPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_signup_page(browser):
    browser.get(browser.url + '/index.php?route=account/register')
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignupPage.FIRST_NAME_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignupPage.LAST_NAME_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignupPage.EMAIL_INPUT))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(SignupPage.PASSWORD_BLOCK))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(SignupPage.FORM_CHECK))
