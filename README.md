# Secure Coding Review Project

## Overview

This project was developed as part of a Cybersecurity Internship Task focused on **Secure Coding Review**. The objective was to create a Flask-based web application, identify security vulnerabilities through manual code review and static analysis, and implement remediation measures following secure coding best practices.

The project contains both a **vulnerable version** (`app.py`) and a **secure version** (`secure_app.py`) to demonstrate the identification and mitigation of common web application security flaws.

---

## Objectives

* Develop a web application using Python and Flask.
* Perform a secure coding review.
* Identify security vulnerabilities.
* Conduct manual code inspection.
* Perform static analysis using Bandit.
* Implement security fixes.
* Compare vulnerable and secure implementations.
* Document findings and recommendations.

---

## Technology Stack

| Component              | Technology   |
| ---------------------- | ------------ |
| Programming Language   | Python       |
| Framework              | Flask        |
| Database               | SQLite       |
| Frontend               | HTML, CSS    |
| Security Analysis Tool | Bandit       |
| Version Control        | Git & GitHub |

---

## Project Structure

```text
SECURE CODING REVIEW/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── search.html
│
├── app.py
├── secure_app.py
├── users.db
├── bandit_report.txt
├── Review_Report.pdf
└── README.md
```

---

## Features

### Vulnerable Application (app.py)

* User Registration
* User Login
* Dashboard Access
* Search Functionality
* Intentionally Vulnerable Components

### Secure Application (secure_app.py)

* Secure Authentication
* Password Hashing
* Parameterized Queries
* XSS Protection
* Secure Session Handling
* Improved Configuration Management

---

## Vulnerabilities Identified

### 1. SQL Injection

**Severity:** High

The login functionality was vulnerable to SQL Injection due to unsafe query construction.

**Impact:**

* Authentication bypass
* Unauthorized access
* Database manipulation

**Remediation:**

* Parameterized SQL queries

---

### 2. Cross-Site Scripting (XSS)

**Severity:** High

User input was rendered without proper output encoding.

**Impact:**

* JavaScript execution
* Session theft
* Client-side attacks

**Remediation:**

* Template escaping
* Input validation

---

### 3. Plain Text Password Storage

**Severity:** High

Passwords were stored directly in the database.

**Impact:**

* Credential exposure
* Account compromise

**Remediation:**

* Password hashing using Werkzeug

---

### 4. Hardcoded Secret Key

**Severity:** Medium

Sensitive application secrets were stored directly in source code.

**Impact:**

* Session security risks
* Configuration exposure

**Remediation:**

* Environment variables

---

### 5. Debug Mode Exposure

**Severity:** Medium

Debug mode was enabled in the production configuration.

**Impact:**

* Information disclosure
* Increased attack surface

**Remediation:**

* Disable debug mode

---

## Static Analysis

Static code analysis was performed using **Bandit**.

### Scan Command

```bash
bandit -r .
```

### Purpose

* Identify insecure coding practices
* Improve application security
* Support manual code review

---

## Security Improvements Implemented

| Vulnerability               | Vulnerable Version | Secure Version |
| --------------------------- | ------------------ | -------------- |
| SQL Injection               | Present            | Fixed          |
| XSS                         | Present            | Fixed          |
| Plain Text Password Storage | Present            | Fixed          |
| Hardcoded Secret Key        | Present            | Fixed          |
| Debug Mode Enabled          | Present            | Fixed          |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/SecureCodingReview.git
```

### Navigate to Project Directory

```bash
cd SecureCodingReview
```

### Install Dependencies

```bash
pip install flask werkzeug bandit
```

### Run Vulnerable Application

```bash
python app.py
```

### Run Secure Application

```bash
python secure_app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Learning Outcomes

Through this project, the following concepts were learned:

* Secure Coding Principles
* Vulnerability Assessment
* SQL Injection Analysis
* Cross-Site Scripting Analysis
* Secure Authentication
* Password Hashing
* Static Application Security Testing (SAST)
* Flask Security Best Practices
* Secure Configuration Management

---

## Report

The detailed project report is available in:

```text
Review_Report.pdf
```

The report includes:

* Vulnerability Analysis
* Severity Assessment
* Security Recommendations
* Static Analysis Results
* Remediation Techniques
* Secure Coding Best Practices

---

## Author

Lavanya

Cybersecurity Internship Project

Secure Coding Review and Vulnerability Assessment using Python Flask
