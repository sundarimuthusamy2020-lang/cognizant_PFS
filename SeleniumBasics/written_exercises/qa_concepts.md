# Hands-On 1 – QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Testing Types for the Course Management API

### 1. Test Cases for Each Testing Level

#### Unit Testing

* **Scenario:** Verify that the `create_course()` function correctly creates a course object when valid input is provided.
* **Expected Result:** A course object is created with the supplied course details.
* **Classification:** Functional Testing

#### Integration Testing

* **Scenario:** Verify that the `POST /api/courses/` endpoint successfully stores course information in the database.
* **Expected Result:** The API returns HTTP 201 Created, and the course record exists in the database.
* **Classification:** Functional Testing

#### System Testing

* **Scenario:** Submit a new course using the API, retrieve it using the GET endpoint, update it, and finally delete it.
* **Expected Result:** Every operation completes successfully and the database reflects each change correctly.
* **Classification:** Functional Testing

#### User Acceptance Testing (UAT)

* **Scenario:** A college administrator creates a new course through the application and verifies that it appears in the course list.
* **Expected Result:** The administrator can complete the task without errors and the new course is visible.
* **Classification:** Functional Testing

---

### 2. Functional vs Non-Functional Testing

Functional testing verifies whether the application behaves according to the specified requirements.

Examples:

* Creating a course
* Updating a course
* Deleting a course
* Retrieving course details

Non-functional testing evaluates how well the application performs.

**Example: Performance Testing**

* Send 500 concurrent requests to `POST /api/courses/`.
* Expected Result: Average response time remains below 2 seconds without failures.

---

### 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing                                                | White-Box Testing                            |
| ---------------------------------------------------------------- | -------------------------------------------- |
| Tests application functionality without viewing the source code. | Tests the internal code structure and logic. |
| Focuses on inputs and expected outputs.                          | Focuses on code paths, branches, and logic.  |
| Usually performed by QA/Test Engineers.                          | Usually performed by Developers.             |

---

### 4. Formal Test Cases for `POST /api/courses/`

| Test Case ID | Description                                | Preconditions         | Test Steps                                        | Expected Result                                               | Actual Result | Pass/Fail |
| ------------ | ------------------------------------------ | --------------------- | ------------------------------------------------- | ------------------------------------------------------------- | ------------- | --------- |
| TC001        | Create course with valid data              | API is running        | 1. Send POST request with valid course details.   | HTTP 201 Created. Course is stored successfully.              |               |           |
| TC002        | Create course with missing mandatory field | API is running        | 1. Send POST request without Course Name.         | HTTP 400 Bad Request with validation message.                 |               |           |
| TC003        | Create duplicate course                    | Course already exists | 1. Send POST request using an existing Course ID. | Appropriate error message (409 Conflict or validation error). |               |           |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
New
  ↓
Assigned
  ↓
Open
  ↓
Fixed
  ↓
Retest
  ↓
Verified
  ↓
Closed
```

### Alternative Paths

**Rejected**

* The defect is invalid, cannot be reproduced, or is working as designed.

**Deferred**

* The defect is valid but fixing it is postponed to a future release due to low priority or project constraints.

---

## 6. Severity and Priority Classification

### a) POST `/api/courses/` returns HTTP 500 for all requests

* **Severity:** Critical
* **Priority:** P1
* **Justification:** Core functionality is completely unavailable and users cannot create courses.

---

### b) Course names longer than 150 characters are silently truncated

* **Severity:** Medium
* **Priority:** P3
* **Justification:** Data integrity is affected, but the application continues functioning.

---

### c) Swagger documentation contains a typo

* **Severity:** Low
* **Priority:** P4
* **Justification:** Cosmetic issue with no impact on application functionality.

---

### d) Login occasionally returns HTTP 401 for valid credentials

* **Severity:** High
* **Priority:** P1
* **Justification:** Users may be unable to access the application. Since the issue is intermittent, it can be difficult to diagnose and should be addressed urgently.

---

## 7. Defect Report

**Defect ID:** DEF-001

**Title:**
POST `/api/courses/` returns HTTP 500 Internal Server Error for valid requests.

**Environment:**

* Windows 11
* Python 3.10
* Chrome Browser
* FastAPI Application

**Build Version:**
v1.0.0

**Severity:**
Critical

**Priority:**
P1

**Steps to Reproduce:**

1. Start the application.
2. Open Postman or Swagger UI.
3. Send a valid POST request to `/api/courses/`.
4. Observe the response.

**Expected Result:**
The API should return **HTTP 201 Created** and store the course successfully.

**Actual Result:**
The API returns **HTTP 500 Internal Server Error** and no course is created.

**Attachments:**
Screenshot of 500 error.

---

## 8. Difference Between Severity and Priority

**Severity** refers to the impact of a defect on the system's functionality.

**Priority** refers to how urgently the defect should be fixed.

### Example

A spelling mistake on the CEO's dashboard is a **Low Severity** issue because it does not affect functionality. However, it may be assigned **High Priority (P1)** because it is highly visible before an important customer presentation.

This example shows that a defect can have **Low Severity but High Priority** depending on business needs.
