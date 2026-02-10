# 🏥 Clinic Management SaaS (Multi-Tenant)

A **production-grade, multi-tenant Clinic Management SaaS** built using **Django**.  
Designed with **real-world architecture**, **data isolation**, and **role-based access control**.

This is **not a tutorial project** — it focuses on **scalable design decisions** commonly expected in interviews and production systems.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- Custom user model
- Session-based authentication
- Role-Based Access Control (RBAC)
- Secure login/logout flow
- `next` parameter handling after login

### 🏢 Multi-Tenant Architecture
- **Clinic = Tenant**
- Single database with **logical data isolation**
- Every user belongs to exactly one clinic
- All queries scoped using `user.clinic`

### 👥 Roles & Permissions
| Role   | Permissions |
|------|------------|
| Admin | Manage clinic, doctors, staff |
| Doctor | View own appointments |
| Staff | Limited operational access |

### 🧑‍⚕️ Clinic Operations
- Doctor management
- Patient records
- Appointment scheduling
- Dashboard overview

### 🛠 Django Admin
- Customized admin panel
- Internal back-office tooling
- Bootstrap data management

---

## 🧠 Tech Stack

- **Backend**: Django 4.2
- **Database**: SQLite (temporary)
- **Auth**: Custom User Model
- **Frontend**: Django Templates
- **Security**: CSRF, session auth
- **Architecture**: Multi-app modular design

---

## 🧩 Project Structure

clinic_saas/
│
├── apps/
│ ├── accounts/ # Custom user, auth, roles
│ ├── clinic/ # Clinic (tenant) logic
│ ├── dashboard/ # Core UI views
│ ├── patients/ # Patient management
│ ├── appointments/ # Scheduling logic
│
├── templates/
│ ├── base.html
│ ├── accounts/
│ └── dashboard/
│
├── static/
├── manage.py
└── requirements.txt

---

## 🔑 Core Design Decisions (Interview Ready)

### ✅ Custom User Model
- Implemented from day one
- Supports roles and tenant linkage
- Avoids risky migrations later

```python
AUTH_USER_MODEL = 'accounts.User'
<img width="1890" height="875" alt="Screenshot 2026-02-09 222802" src="https://github.com/user-attachments/assets/e275cfbe-9e50-4434-9f4a-b8926e67d897" />
<img width="1883" height="866" alt="Screenshot 2026-02-09 222751" src="https://github.com/user-attachments/assets/a9e01d4f-5d69-44c9-907c-459c123abf93" />
<img width="1885" height="856" alt="Screenshot 2026-02-09 222744" src="https://github.com/user-attachments/assets/b6a97b62-4732-463a-9192-41c01378a4fa" />
<img width="1887" height="863" alt="Screenshot 2026-02-09 222737" src="https://github.com/user-attachments/assets/065f5a66-b083-4499-8871-edbcbfa8e810" />
<img width="1884" height="879" alt="Screenshot 2026-02-09 222730" src="https://github.com/user-attachments/assets/1ec89a5d-88c3-4e4b-9796-60c9130b04b1" />





