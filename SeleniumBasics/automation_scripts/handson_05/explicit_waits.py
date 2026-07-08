"""
Hands-On 5 - Task 2

Explicit Waits
Sleep
Clickable
Fluent Wait
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager(driver_version="149.0.7827.201").install()
    )
)

driver.maximize_window()

try:

    driver.get(
        "https://testmuai.com/selenium-playground/bootstrap-alert-messages-demo/"
    )

    wait = WebDriverWait(driver, 10)

    # --------------------------------------------------------
    # Wait until Success button is clickable
    # --------------------------------------------------------

    success_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'Autoclosable Success Message')]"
            )
        )
    )

    start = time.time()

    success_btn.click()

    # --------------------------------------------------------
    # Wait until success message exists
    # --------------------------------------------------------

    success_alert = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(text(),'Autocloseable success message')]"
            )
        )
    )

    end = time.time()

    print("Explicit Wait:", round(end - start, 3), "seconds")
    print(success_alert.text)

    assert "success" in success_alert.text.lower()

    print("Explicit Wait Passed")

    # --------------------------------------------------------
    # time.sleep Demo
    # --------------------------------------------------------

    driver.refresh()

    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'Autoclosable Success Message')]"
            )
        )
    ).click()

    start = time.time()

    time.sleep(3)

    success_alert = driver.find_element(
        By.XPATH,
        "//div[contains(text(),'Autocloseable success message')]"
    )

    end = time.time()

    print("Sleep:", round(end - start, 3), "seconds")

    # --------------------------------------------------------
    # Fluent Wait
    # --------------------------------------------------------

    driver.get(
        "https://testmuai.com/selenium-playground/table-sort-search-demo/"
    )

    fluent_wait = WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=0.5,
        ignored_exceptions=[NoSuchElementException]
    )

    first_row = fluent_wait.until(
        lambda d: d.find_element(
            By.CSS_SELECTOR,
            "#example tbody tr"
        )
    )

    print("\nFirst Row")
    print(first_row.text)

    print("\nHands-On 5 Task 2 Completed Successfully")

finally:
    driver.quit()