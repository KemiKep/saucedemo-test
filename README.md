# E2E тест для сайта saucedemo.com

Этот проект содержит автоматический end-to-end (e2e) тест для проверки сценария покупки товара на сайте [saucedemo.com](https://www.saucedemo.com) с использованием Python и Selenium.

## Описание сценария теста

Тест выполняет следующие шаги:

1. Авторизация на сайте с использованием тестового аккаунта:
   - Логин: `standard_user`
   - Пароль: `secret_sauce`
2. Выбор товара ("Sauce Labs Backpack") и добавление его в корзину.
3. Переход в корзину и проверка, что товар добавлен.
4. Оформление покупки и заполнение всех необходимых полей.
5. Завершение покупки.
6. Проверка, что покупка завершена успешно.

## Установка

1. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Запуск теста

1. Запустите тест:

    ```bash
    python test_purchase.py
    ```

## Требования

- Python 3.x
- Selenium
