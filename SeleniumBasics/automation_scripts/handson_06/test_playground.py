import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# --------------------------------------------------
# Simple Form Demo (Parameterized)
# --------------------------------------------------

@pytest.mark.parametrize(
    "message",
    ["Hello", "Selenium Automation", "12345"]
)
def test_simple_form_submission(driver, base_url, message):

    driver.get(base_url + "simple-form-demo")

    # Wait until page is fully loaded
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # Handle cookie banner if present
    try:
        cookie_btn = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Accept') or contains(.,'Allow')]")
            )
        )
        cookie_btn.click()
    except:
        pass

    input_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "user-message"))
    )

    input_box.clear()
    input_box.send_keys(message)

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "showInput"))
    )

    # Scroll to button
    driver.execute_script("arguments[0].scrollIntoView(true);", button)

    # Click using JavaScript
    driver.execute_script("arguments[0].click();", button)

    # Wait until the message changes
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "message").text.strip() == message
    )

    assert driver.find_element(By.ID, "message").text.strip() == message
# --------------------------------------------------
# Dropdown Demo
# --------------------------------------------------

def test_dropdown_selection(driver, base_url):

    driver.get(base_url + "select-dropdown-demo")

    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "select-demo"))
    )

    select = Select(dropdown)
    select.select_by_visible_text("Wednesday")

    assert select.first_selected_option.text == "Wednesday"