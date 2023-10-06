import time
import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Navigate the web page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(2)

        # Type username student into Username field
        user_locator = driver.find_element(By.ID, "username")
        user_locator.send_keys('student')

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button.click()
        time.sleep(5)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        current_URL = driver.current_url
        expected_URL = "https://practicetestautomation.com/logged-in-successfully/"
        assert current_URL == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page"""
        logout_button = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button.is_displayed()

        driver.quit()
