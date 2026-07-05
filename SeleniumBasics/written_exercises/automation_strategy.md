# Hands-On 3 – Test Automation Process, Lifecycle & Framework Types

# Task 1: Automation Decision and Test Case Selection

## 1. Criteria for Deciding Whether to Automate a Test Case

### Criterion 1: Repetitive Execution

Tests that are executed frequently are good candidates for automation.

**Application:**
The `POST /api/courses/` endpoint is likely to be tested after every code change, making it an excellent automation candidate.

---

### Criterion 2: Regression Testing

Regression tests ensure existing functionality continues to work after changes.

**Application:**
Creating a course is a core API feature that should always be included in regression testing.

---

### Criterion 3: Stable Functionality

Features that rarely change are easier and more cost-effective to automate.

**Application:**
The basic functionality of the `POST /api/courses/` endpoint is expected to remain stable.

---

### Criterion 4: Data-Driven Testing

Tests requiring multiple input combinations benefit greatly from automation.

**Application:**
The endpoint can be tested using various valid and invalid course names, codes, and descriptions.

---

### Criterion 5: High Business Impact

Critical business functions should be automated to detect failures quickly.

**Application:**
Creating courses is a primary function of the Course Management API, so automated verification is essential.

---

# 2. Manual vs Automation Decisions

| Test Case                                                      | Decision     | Justification                                                             |
| -------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------- |
| Regression test for all CRUD endpoints after every code change | **Automate** | Frequently executed and ideal for regression testing.                     |
| Exploratory testing of a new search feature                    | **Manual**   | Requires human creativity and investigation.                              |
| Performance test with 100 concurrent users                     | **Automate** | Load testing tools can repeatedly execute this scenario.                  |
| UI login form testing                                          | **Automate** | Login is a stable and frequently tested feature.                          |
| Verify Swagger documentation accuracy                          | **Manual**   | Requires reviewing documentation content for correctness and readability. |
| Smoke test after deployment                                    | **Automate** | Quick validation after every deployment should be automated.              |

---

# 3. Test Automation ROI

**Definition**

Test Automation Return on Investment (ROI) measures whether the time and cost of developing automated tests are justified by the time saved during repeated execution.

### Given

* Automation development time = **4 hours**
* Manual execution time = **30 minutes (0.5 hours)**

### Break-even Calculation

Automation cost:

**4 hours**

Manual execution cost after *n* runs:

**0.5 × n hours**

Break-even occurs when:

0.5 × n = 4

n = 8

Therefore, **after 8 executions**, the automated test begins to save time compared with manual testing.

### Maintenance Overhead

After the 10th execution, each automated run requires approximately:

20% of 30 minutes = **6 minutes**

Although maintenance slightly increases the total effort, automation continues to provide significant time savings over repeated executions.

---

# 4. Flaky Tests

### Definition

A flaky test is a test that sometimes passes and sometimes fails without any changes to the application being tested.

### Example

A Selenium test clicks a button immediately after opening a page. Sometimes the button loads slowly, causing the test to fail intermittently.

### Preventing Flaky Tests

1. Use Explicit Waits instead of fixed delays.
2. Use stable and unique element locators (ID, Name, CSS).
3. Ensure each test starts with clean test data and an independent environment.

---

# Task 2: Automation Framework Types

## 5. Framework Comparison

### Linear Framework

**Description**

Tests are written as a single sequential script where each action follows the previous one without reusable components.

**Advantage**

Simple to learn and implement.

**Disadvantage**

Poor maintainability and high code duplication.

**Example**

Automating a single login workflow for demonstration purposes.

---

### Modular Framework

**Description**

The application is divided into modules, and reusable functions are created for each module.

**Advantage**

Code reuse reduces maintenance effort.

**Disadvantage**

Managing dependencies between modules can become complex.

**Example**

Separate modules for Login, Course Management, and Student Management.

---

### Data-Driven Framework

**Description**

Test data is stored separately (CSV, Excel, JSON), allowing one script to execute multiple data combinations.

**Advantage**

Large numbers of test cases can be executed with minimal code changes.

**Disadvantage**

Requires additional effort to manage external data sources.

**Example**

Testing course creation using many combinations of course names and codes.

---

### Keyword-Driven Framework

**Description**

Tests are created using predefined keywords such as Login, Click, EnterText, and Verify, allowing non-programmers to contribute.

**Advantage**

Business users can participate in test creation.

**Disadvantage**

Framework development and maintenance are more complex.

**Example**

Business analysts define login and course creation steps using keywords.

---

### Hybrid Framework

**Description**

Combines Modular, Data-Driven, and Keyword-Driven approaches to maximize flexibility and maintainability.

**Advantage**

Highly reusable, scalable, and suitable for enterprise projects.

**Disadvantage**

Initial setup requires more planning and development effort.

**Example**

Large Selenium automation suites with Page Object Model, external test data, reusable utilities, and shared libraries.

---

# 6. Recommended Framework

### Recommendation

A **Hybrid Framework** combining:

* Modular Framework
* Data-Driven Framework
* Keyword-Driven Framework

### Justification

* Login steps can be reused across 20 test cases using reusable modules.
* Fifty user/password combinations can be stored in external data files and executed automatically.
* Keyword-driven components enable non-technical team members to create or maintain test scenarios.
* The framework remains scalable and maintainable as the project grows.

---

# 7. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/
│
├── config/
│   └── config.py
│
├── test_data/
│   ├── login_data.csv
│   └── course_data.csv
│
├── page_objects/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── course_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_courses.py
│   └── test_smoke.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── logger.py
│   └── helpers.py
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
│
└── pytest.ini
```

### Folder Purpose

* **config/** – Stores configuration settings such as URLs and browser options.
* **test_data/** – Contains external test data (CSV, JSON, Excel).
* **page_objects/** – Implements the Page Object Model for each page.
* **tests/** – Contains all automated test cases.
* **utilities/** – Provides reusable helper methods, logging, and WebDriver setup.
* **reports/** – Stores generated test execution reports.
* **screenshots/** – Saves screenshots captured during test failures.
* **requirements.txt** – Lists project dependencies.
* **pytest.ini** – Stores pytest configuration settings.
