import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver,username,password,expected_error_message):
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Open page
        driver.maximize_window()

        # Type username incorrect User into Username field
        user_locator = driver.find_element(By.ID, "username")
        user_locator.send_keys(username)

        # Type password Password123 into password field.
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button.click()
        time.sleep(5)

        # Verify error message is displayed.
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error Message is not displayed, expected to be displayed."

        # Verify error message text is 'Your username is invalid!'
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not as expected."

    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()

        # Type username incorrect User into Username field
        user_locator = driver.find_element(By.ID, "username")
        user_locator.send_keys("incorrectUser")

        # Type password Password123 into password field.
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button.click()
        time.sleep(5)

        # Verify error message is displayed.
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error Message is not displayed, expected to be displayed."

        # Verify error message text is 'Your username is invalid!'
        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not as expected."

    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()

        # Type username incorrect User into Username field
        user_locator = driver.find_element(By.ID, "username")
        user_locator.send_keys("student")

        # Type password Password123 into password field.
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button.click()
        time.sleep(5)

        # Verify error message is displayed.
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error Message is not displayed, expected to be displayed."

        # Verify error message text is 'Your password is invalid!'
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not as expected."
