# Finance Data Processing and Access Control Backend

## Overview

This project is a backend system for a finance dashboard that manages financial records, user roles, and summary analytics. It is designed to demonstrate backend architecture, API design, data modeling, business logic, and access control.

The system allows different types of users to interact with financial data based on their roles and provides aggregated insights for dashboard visualization.

---

## Features

### User & Role Management

* Create and manage users
* Assign roles: Admin, Analyst, Viewer
* Manage user status (active/inactive)

### Financial Records Management

* Create, read, update, delete financial records
* Fields include:

  * Amount
  * Type (income/expense)
  * Category
  * Date
  * Notes
* Filter records by:

  * Category
  * Type
  * Date range
* Pagination support for large datasets
* Search support using query parameter

### Dashboard Analytics

* Total income
* Total expenses
* Net balance
* Category-wise totals
* Recent activity

### Role-Based Access Control (RBAC)

* Admin → Full access (CRUD operations)
* Analyst → Read-only access
* Viewer → Read-only access

### Validation & Error Handling

* Input validation (e.g., positive amount)
* Proper error responses and status codes

---

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default database)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd finance_dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the server

```bash
python manage.py runserver
```

### 5. Access APIs

```
http://127.0.0.1:8000/api/
```

---

## API Endpoints

### Users

| Method | Endpoint         | Description |
| ------ | ---------------- | ----------- |
| GET    | /api/users/      | List users  |
| POST   | /api/users/      | Create user |
| PUT    | /api/users/{id}/ | Update user |
| DELETE | /api/users/{id}/ | Delete user |

---

### Records

| Method | Endpoint           | Description   |
| ------ | ------------------ | ------------- |
| GET    | /api/records/      | List records  |
| POST   | /api/records/      | Create record |
| PUT    | /api/records/{id}/ | Update record |
| DELETE | /api/records/{id}/ | Delete record |

#### Filtering Examples

```
/api/records/?category=salary
/api/records/?type=income
/api/records/?start_date=2026-04-01&end_date=2026-04-06
```

#### Search Examples

```
/api/records/?search=salary
/api/records/?type=income&search=salary
```

---

### Dashboard

| Method | Endpoint                | Description           |
| ------ | ----------------------- | --------------------- |
| GET    | /api/dashboard/summary/ | Get summary analytics |

#### Example Response

```json
{
  "total_income": 5000,
  "total_expense": 2000,
  "net_balance": 3000,
  "category_totals": [
    {"category": "salary", "total": 5000},
    {"category": "food", "total": 2000}
  ],
  "recent_activity": [...]
}
```

---

## Role-Based Access Control

Access is controlled using a custom permission system.

| Role    | Permissions                   |
| ------- | ----------------------------- |
| Admin   | Full access (CRUD operations) |
| Analyst | Read-only access              |
| Viewer  | Read-only access              |

### How Role is Passed

Role is passed via request header:

```
Role: ADMIN
Role: ANALYST
Role: VIEWER
```

---

## Status Codes

| Code | Meaning     |
| ---- | ----------- |
| 200  | Success     |
| 201  | Created     |
| 400  | Bad Request |
| 403  | Forbidden   |
| 404  | Not Found   |

---

## Validation Rules

* Amount must be positive
* Type must be either `income` or `expense`
* Required fields must be provided

---

## Assumptions

* Authentication is not implemented; role is passed via headers
* `created_by` is manually assigned (for simplicity, authentication is not implemented)
* Dates are expected in `YYYY-MM-DD` format
* SQLite is used for simplicity

---

## Optional Enhancements (Future Scope)

* JWT Authentication
* Soft delete support
* API documentation (Swagger)
* Unit and integration testing

---

## Project Highlights

* Clean and modular backend structure
* Proper separation of concerns (models, views, serializers)
* Real-world backend features like RBAC, filtering, search, and analytics
* Focus on maintainability and scalability

---

## Conclusion

This project demonstrates backend engineering principles including API design, data handling, access control, and business logic implementation. It is designed to be simple yet structured, focusing on clarity and correctness.

---

## Submission

GitHub Repository: <your-repo-link>
