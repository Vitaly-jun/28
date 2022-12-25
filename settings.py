baseUrl = 'https://b2c.passport.rt.ru'

registerFormKeysName = ['A', 'Ab', '!@#$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', 'Имя']
registerFormKeysLastName = ['A', 'Ab', '!@#$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', 'Фамилия']
registerFormKeys = ['A', '!@#$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', '9133000500', 'test@email.ru']
registerPassword = ['абвгдабв', 'passw', 'password', 'password1', 'Password1']
registerKeysDict = {
    'firstName': registerFormKeysName,
    'lastName': registerFormKeysLastName
}

registerErrorsName = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
registerErrors = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
errorPassword = 'Длина пароля должна быть не менее 8 символов'

exampleKeys = ['7913300500', 'test@email.ru', 'login1', 'firstName']
placeValue = ['Мобильный телефон', 'Электронная почта', 'Лицевой счёт', 'Логин']
tabTitlesAuth = ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
activeTab = 'rt-tab--active'
