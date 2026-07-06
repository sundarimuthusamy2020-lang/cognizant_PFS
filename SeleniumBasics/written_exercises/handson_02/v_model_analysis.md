# Hands-On 2 – SDLC vs TDLC: V-Model & Agile QA Integration

# Task 1: V-Model Mapping

## 1. V-Model Diagram

```text
                 SDLC (Development)

             Requirements
                  │
                  │
             System Design
                  │
                  │
          Architecture Design
                  │
                  │
             Module Design
                  │
                  │
                Coding
                  ▲
                  │
             Unit Testing
                  │
                  │
         Integration Testing
                  │
                  │
           System Testing
                  │
                  │
        Acceptance Testing

              TDLC (Testing)
```

### SDLC to TDLC Mapping

| SDLC Phase            | Corresponding TDLC Phase        | Test Artifact Produced                        |
| --------------------- | ------------------------------- | --------------------------------------------- |
| Requirements Analysis | Acceptance Testing              | Acceptance Test Plan, Acceptance Test Cases   |
| System Design         | System Testing                  | System Test Plan, System Test Cases           |
| Architecture Design   | Integration Testing             | Integration Test Plan, Integration Test Cases |
| Module Design         | Unit Testing                    | Unit Test Cases, Unit Test Plan               |
| Coding                | Execution of all testing levels | Source Code and Executable Application        |

---

## 2. Entry and Exit Criteria

### Unit Testing

**Entry Criteria**

* Module development is complete.
* Source code is compiled successfully.
* Unit test cases are prepared.

**Exit Criteria**

* All unit test cases executed.
* All critical defects fixed.
* Code coverage meets project standards.

---

### Integration Testing

**Entry Criteria**

* Individual modules have passed unit testing.
* Modules are integrated.
* Integration test cases are ready.

**Exit Criteria**

* Interfaces between modules work correctly.
* Critical integration defects are resolved.
* Integration test cases completed.

---

### System Testing

**Entry Criteria**

* Complete application is deployed.
* System test cases are approved.
* Test environment is available.

**Exit Criteria**

* All planned system test cases executed.
* No open Critical or High severity defects.
* System meets functional requirements.

---

### Acceptance Testing

**Entry Criteria**

* System testing completed successfully.
* Product is stable.
* Customer or business users are available.

**Exit Criteria**

* Customer approves the application.
* Acceptance criteria are satisfied.
* Product is ready for release.

---

## 3. Early QA Engagement in the V-Model

### Requirements Review

QA participates during requirement analysis to:

* Identify ambiguous or incomplete requirements.
* Ensure every requirement is testable.
* Prepare acceptance criteria early.

### Design Review

QA reviews the system design to:

* Identify potential testing challenges.
* Prepare integration and system test scenarios.
* Ensure the design supports testing.

---

# Task 2: Agile QA and Shift-Left Testing

## 4. Problems with Waterfall Testing

### Problem 1: Late Defect Detection

Testing starts only after development is complete, making defects more expensive and time-consuming to fix.

---

### Problem 2: Requirement Misunderstandings

If requirements are misunderstood, the issue may not be discovered until system testing, leading to significant rework.

---

### Problem 3: Release Delays

Large numbers of defects found near the end of the project can delay delivery and increase project costs.

---

## 5. QA Responsibilities in Agile Ceremonies

### Sprint Planning

* Review user stories.
* Define acceptance criteria.
* Estimate testing effort.
* Identify testing risks.

---

### Daily Stand-up

* Report testing progress.
* Discuss blockers.
* Coordinate with developers on defect fixes.

---

### Sprint Review

* Verify completed user stories.
* Demonstrate tested features.
* Confirm acceptance criteria are satisfied.

---

### Sprint Retrospective

* Discuss testing improvements.
* Identify process bottlenecks.
* Suggest better automation and collaboration practices.

---

## 6. Shift-Left Testing Practices

### a) Review Requirements for Testability

QA reviews requirements before development to ensure they are complete, clear, and testable.

---

### b) Write Test Cases Before Coding (TDD/BDD)

QA prepares test cases and acceptance scenarios before implementation so developers clearly understand expected behavior.

---

### c) Static Code Analysis

Developers use static analysis tools to identify coding issues, security vulnerabilities, and coding standard violations before execution.

---

### d) API Contract Testing Before Integration

QA validates API request and response formats against the API specification before integrating with other services, reducing integration defects.

---

## 7. Acceptance Criteria (Given-When-Then)

### Scenario 1 – Successful Course Creation

**Given**
A college administrator is logged into the system.

**When**
The administrator enters a unique course code and valid course details, then submits the form.

**Then**
The course is created successfully and a confirmation message is displayed.

---

### Scenario 2 – Duplicate Course Code

**Given**
A course with the same course code already exists.

**When**
The administrator attempts to create another course using that course code.

**Then**
The system displays an error message indicating that the course code already exists, and no duplicate course is created.

---

### Scenario 3 – Missing Required Fields

**Given**
The administrator opens the Create Course form.

**When**
The administrator submits the form without entering one or more mandatory fields.

**Then**
The system displays validation messages for the missing fields and prevents course creation.
