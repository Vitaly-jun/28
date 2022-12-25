from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import settings


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en-GB'})
    driver = webdriver.Chrome(chrome_options=options)

    driver.get(settings.baseUrl)
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)
    assert wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="card-container__title"]'))).text == 'Авторизация'
    return driver, wait


def test_correct_redirect_register():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'
    driver.quit()


def test_Name_and_lastName_register():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    firstNameInput = wait.until(EC.presence_of_element_located((By.NAME, 'firstName')))
    lastNameInput = wait.until(EC.presence_of_element_located((By.NAME, 'lastName')))

    elementsDictionary = {
        'firstName': firstNameInput,
        'lastName': lastNameInput
    }

    for key in settings.registerKeysDict:
        values = settings.registerKeysDict[key]

        actionChain.click(elementsDictionary[key]).perform()

        for j in range(len(values)):
            actionChain.send_keys(values[j]).perform()
            driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

            if j < len(values) - 1:
                if j >= 1:
                    pass
                else:
                    error = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error'))).text
                assert error == settings.registerErrorsName
                actionChain.double_click(elementsDictionary[key]).click_and_hold().send_keys(Keys.DELETE).perform()
    driver.quit()


def test_register_email_and_phone():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    addressNameInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address')))

    values = settings.registerFormKeys
    actionChain.click(addressNameInput).perform()

    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
            else:
                error = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error'))).text
            assert error == settings.registerErrors
            actionChain.double_click(addressNameInput).click_and_hold().send_keys(Keys.DELETE).perform()
    driver.quit()


def test_register_password():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    passNameInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password')))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div > div > div:nth-of-type(2) > svg'))).click()

    values = settings.registerPassword
    actionChain.click(passNameInput).perform()

    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
            else:
                error = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error'))).text
            actionChain.double_click(passNameInput).click_and_hold().send_keys(Keys.DELETE).perform()
            assert error == settings.errorPassword
    driver.quit()


def test_register_password_password():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div > div > div:nth-of-type(2) > svg'))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('Password1').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > div > div:nth-of-type(2) > svg > path'))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('error_password').perform()
    driver.find_element(By.NAME, 'register').click()

    error = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Пароли не совпадают')]"))).text
    assert error == 'Пароли не совпадают'
    driver.quit()


def test_registration_phone():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).click()
    actionChain.send_keys('Имя').perform()
    wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).click()
    actionChain.send_keys('Фамилия').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address'))).click()
    actionChain.send_keys('+79133000500').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('Password1').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('Password1').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div > div > div:nth-of-type(2) > svg'))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > div > div:nth-of-type(2) > svg > path'))).click()
    driver.find_element(By.NAME, 'register').click()

    confirmPage = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Подтверждение телефона')]"))).text
    assert confirmPage == 'Подтверждение телефона'
    driver.quit()


def test_registration_email():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).click()
    actionChain.send_keys('Имя').perform()
    wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).click()
    actionChain.send_keys('Фамилия').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address'))).click()
    actionChain.send_keys('test@email.ru').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('Password1').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('Password1').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div > div > div:nth-of-type(2) > svg'))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > div > div:nth-of-type(2) > svg > path'))).click()
    driver.find_element(By.NAME, 'register').click()

    confirmPage = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Подтверждение email')]"))).text
    assert confirmPage == 'Подтверждение email'
    driver.quit()


def test_click_forgotPassword():
    driver, wait = get_driver()

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()

    assert wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]"))).text == 'Восстановление пароля'
    driver.quit()


def test_back_login():
    driver, wait = get_driver()

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]"))).text == 'Восстановление пароля'

    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-back']"))).click()
    assert wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]"))).text == 'Авторизация'
    driver.quit()


def test_correct_change_input():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    tabButtons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rt-tab')))
    placeholderInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
    assert placeholderInput == settings.placeValue[0]

    for i in range(len(tabButtons)):
        actionChain.move_to_element(driver.find_element(By.ID, 'username')).click().perform()
        actionChain.send_keys(settings.exampleKeys[i]).perform()
        actionChain.move_to_element(driver.find_element(By.ID, 'password')).click().perform()
        activeTabButton = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.rt-tabs .{settings.activeTab}')))
        assert activeTabButton.text == settings.tabTitlesAuth[i], driver.quit()

        actionChain.double_click(driver.find_element(By.ID, 'username')).click_and_hold().send_keys(
            Keys.DELETE).perform()

    driver.quit()


def test_refresh_captcha():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]"))).text == 'Восстановление пароля'

    oldCaptcha = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-captcha__image'))).get_attribute('src')
    actionChain.move_to_element(driver.find_element(By.CLASS_NAME, 'rt-captcha__reload')).click().perform()

    driver.implicitly_wait(20)

    newCaptcha = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-captcha__image'))).get_attribute('src')
    assert oldCaptcha != newCaptcha
    driver.quit()


def test_correct_phone_input():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'username'))).click()
    actionChain.send_keys('+79133000500').perform()
    wait.until(EC.presence_of_element_located((By.ID, 'password'))).click()
    actionChain.send_keys('Password1').perform()
    driver.find_element(By.ID, 'kc-login').click()

    info = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div/h2')
    text = info.get_attribute('innerText')
    assert 'Вит' in text
    driver.quit()


def test_correct_email_input():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'username'))).click()
    actionChain.send_keys('test@email.ru').perform()
    wait.until(EC.presence_of_element_located((By.ID, 'password'))).click()
    actionChain.send_keys('Password1').perform()
    driver.find_element(By.ID, 'kc-login').click()

    info = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div/h2')
    text = info.get_attribute('innerText')
    assert 'Вит' in text
    driver.quit()


def test_not_correct_email_input():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'username'))).click()
    actionChain.send_keys('test@email.ru').perform()
    wait.until(EC.presence_of_element_located((By.ID, 'password'))).click()
    actionChain.send_keys('error_password').perform()
    driver.find_element(By.ID, 'kc-login').click()

    info = driver.find_element(By.XPATH, '//*[@id="form-error-message"]')
    text = info.get_attribute('innerText')
    assert 'Неверный логин или пароль' in text
    driver.quit()


def test_correct_login_input():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    wait.until(EC.presence_of_element_located((By.ID, 'username'))).click()
    actionChain.send_keys('login').perform()
    wait.until(EC.presence_of_element_located((By.ID, 'password'))).click()
    actionChain.send_keys('Password1').perform()
    driver.find_element(By.ID, 'kc-login').click()

    info = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div/h2')
    text = info.get_attribute('innerText')
    assert 'Вит' in text
    driver.quit()
