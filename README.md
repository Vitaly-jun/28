Для запуска теста нужно выполнить команду:
python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe test.py
def test_correct_redirect_register():Проверка перехода по ссылке "Зарегистрироваться"
def test_Name_and_lastName_register():Проверка полей Имя и Фамилия, на корректность ввода данных, на странице Регистрации
def test_register_email_and_phone():Проверка полей "Email или Мобильный телефон", на корректность ввода данных , на странице Регистрации
def test_register_password():Проверка корректной работы поля Пароль на странице Регистрации
def test_register_password_password():Проверка корректной работы поля Подтверждение пароля на странице Регистрации
def test_registration_phone():Проверка регистрации по номеру телефона
def test_registration_email():Проверка регистрация по email
def test_click_forgotPassword():Проверка перехода по ссылке "Забыл пароль"
def test_back_login():Проверка перехода по ссылке Вернуться назад с страницы восстановления пароля
def test_correct_change_input():Проверка автоматической смены таба при вводе - телефона/почты/лицевого счета/логина, на странице Авторизации
def test_refresh_captcha():Проверка обновление капчи на странице Восстановления пароля
def test_correct_phone_input():Вход пользователя по номеру телефона с корректными данными
def test_correct_email_input():Вход пользователя по email с корректными данными
def test_not_correct_email_input():Вход пользователя по email с некорректными данными
def test_correct_login_input():Вход пользователя по логину с корректными данными



































