import pytest
from selenium import webdriver


# Base URL fixture
@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


# Chrome Driver fixture
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# Store test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# Screenshot on failure
@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    yield

    rep = getattr(request.node, "rep_call", None)

    if rep and rep.failed:
        driver = request.node.funcargs.get("driver")
        if driver:
            try:
                driver.save_screenshot(f"{request.node.name}_failure.png")
            except Exception:
                pass