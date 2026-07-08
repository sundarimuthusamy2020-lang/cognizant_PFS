"""
Hands-On 5 - Task 1
Locator Strategies

Preference Order (Best → Worst)

1. ID
2. NAME
3. CSS_SELECTOR
4. Relative XPath
5. CLASS_NAME
6. TAG_NAME / Absolute XPath

ID is preferred because it is usually unique and stable.
Absolute XPath is the least preferred because it breaks whenever
the page structure changes.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(driver_version="149").install())
)

driver.maximize_window()
driver.implicitly_wait(10)

try:

    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-message"))
    )

    # -------------------------------------------------
    # ID
    # -------------------------------------------------
    element = driver.find_element(By.ID, "user-message")
    print("✓ Located using ID")

    # -------------------------------------------------
    # NAME
    # -------------------------------------------------
    element = driver.find_element(By.NAME, "message")
    print("✓ Located using NAME")

    # -------------------------------------------------
    # CLASS NAME
    # -------------------------------------------------
    element = driver.find_element(By.CLASS_NAME, "form-control")
    print("✓ Located using CLASS_NAME")

    # -------------------------------------------------
    # TAG NAME
    # -------------------------------------------------
    element = driver.find_element(By.TAG_NAME, "input")
    print("✓ Located using TAG_NAME")

    # -------------------------------------------------
    # ABSOLUTE XPATH
    # -------------------------------------------------
    #
    # Copy a fresh Full XPath from Chrome DevTools if
    # this locator no longer matches the current page.
    #
    try:
        element = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/main/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input"
        )
        print("✓ Located using Absolute XPath")

    except Exception:
        print("⚠ Absolute XPath has changed. Update it using DevTools.")

    # -------------------------------------------------
    # RELATIVE XPATH
    # -------------------------------------------------
    element = driver.find_element(
        By.XPATH,
        "//input[@id='user-message']"
    )

    print("✓ Located using Relative XPath")

    # =====================================================
    # CSS SELECTORS
    # =====================================================

    driver.find_element(
        By.CSS_SELECTOR,
        "#user-message"
    )
    print("✓ CSS by ID")

    driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
    )
    print("✓ CSS by Attribute")

    driver.find_element(
        By.CSS_SELECTOR,
        "form div > input"
    )
    print("✓ CSS Parent > Child")

    # =====================================================
    # CHECKBOX DEMO
    # =====================================================

    driver.get(
        "https://www.lambdatest.com/selenium-playground/checkbox-demo"
    )

    wait.until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "body")
        )
    )

    label = driver.find_element(
        By.XPATH,
        "//label[text()='Option 1']"
    )

    print("\nLabel Found:")
    print(label.text)

    labels = driver.find_elements(
        By.XPATH,
        "//label[contains(text(),'Option')]"
    )

    print("\nAll Option Labels:")

    for lbl in labels:
        print(lbl.text)

    print("\nHands-On 5 Task 1 completed successfully.")

finally:
    driver.quit()