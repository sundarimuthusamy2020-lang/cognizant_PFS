"""
Hands-On 4 - Task 1

Selenium Components

1. WebDriver
- Selenium WebDriver is an API used to automate browser actions.
- It communicates with browser-specific drivers (such as ChromeDriver),
  which in turn communicate with the browser.

2. Selenium Grid
- Selenium Grid allows tests to run in parallel across multiple browsers,
  operating systems, and machines.
- It helps reduce execution time and supports cross-browser testing.

3. Selenium IDE
- Selenium IDE is a browser extension used to record and replay browser actions.
- It is useful for learning Selenium, rapid prototyping, and generating test scripts.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome to run in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Run Chrome without opening a browser window

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(driver_version="149.0.7827.201").install()),
    options=options
)

# Implicit wait
# Implicit waits apply globally to every element lookup.
# This may slow down tests and make failures harder to diagnose.
# Explicit waits are preferred because they wait only for specific elements
# or conditions when required.
driver.implicitly_wait(10)

try:
    driver.get("https://www.lambdatest.com/selenium-playground/")

    print("Page Title:")
    print(driver.title)

finally:
    driver.quit()