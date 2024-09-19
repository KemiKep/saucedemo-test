from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_purchase():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        item_name = "Sauce Labs Backpack"
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == item_name:
                item.find_element(By.TAG_NAME, "button").click()
                print(f"Товар '{name}' добавлен в корзину.")
                break

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        assert item_name in driver.page_source

        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()

        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        print("Полученное сообщение:", success_message.text)
        assert "Thank you for your order!" in success_message.text
        print(f"Покупка товара '{item_name}' завершена успешно.")

    except Exception as e:
        print("Произошла ошибка:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_purchase()