import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(driver_version="149.0.7827.201").install())
)

driver.implicitly_wait(10)

try:
    # Open Selenium Playground
    driver.get("https://www.lambdatest.com/selenium-playground/")

    # Print original window size
    print("Original Window Size:")
    print(driver.get_window_size())

    # Set consistent browser window size
    # A fixed window size ensures responsive UI behaves consistently
    # across different test executions.
    driver.set_window_size(1280, 800)

    print("\nNew Window Size:")
    print(driver.get_window_size())

    # Navigate to Simple Form Demo
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

    # Verify URL
    assert "simple-form-demo" in driver.current_url

    print("\nCurrent URL:")
    print(driver.current_url)

    # Navigate back
    driver.back()

    # Open a new browser tab
    driver.execute_script("window.open('https://www.google.com');")

    # List all open tabs
    print("\nWindow Handles:")
    print(driver.window_handles)

    # Switch to Google tab
    driver.switch_to.window(driver.window_handles[1])

    print("\nGoogle Page Title:")
    print(driver.title)

    # Switch back to Selenium Playground
    driver.switch_to.window(driver.window_handles[0])

    # Take screenshot
    screenshot_file = "playground_screenshot.png"
    driver.save_screenshot(screenshot_file)

    # Verify screenshot exists
    assert os.path.exists(screenshot_file), "Screenshot was not created."

    print(f"\nScreenshot saved successfully as '{screenshot_file}'.")

finally:
    driver.quit()