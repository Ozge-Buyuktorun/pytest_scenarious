import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions")
        driver.maximize_window()

        # Click Add button
        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()

        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # Verify Row 2 input field is displayed.
        assert row2_input_element.is_displayed(), " Row2 input should be displayed, but it is not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_intractable_exception(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions")
        driver.maximize_window()

        # Click Add Button
        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()

        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # Type text into the second input field
        row2_input_element.send_keys("Sushi")

        # Push Save button using locator : By.Name("Save")
        driver.find_element(By.XPATH,"//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']").click()

        # Verify text saved
        confirmation_element= driver.find_element(By.ID,"confirmation")
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "Confirmation message is not expected."