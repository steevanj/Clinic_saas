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

<img width="1890" height="875" alt="Screenshot 2026-02-09 222802" src="https://github.com/user-attachments/assets/4b464765-6ec3-4636-85b3-f6dc9eedec33" />
<img width="1883" height="866" alt="Screenshot 2026-02-09 222751" src="https://github.com/user-attachments/assets/00f0280d-055f-458c-8cdd-6cdbfb2ae70d" />
<img width="1885" height="856" alt="Screenshot 2026-02-09 222744" src="https://github.com/user-attachments/assets/44d2c16e-d6a3-47b9-bb64-5c49161ac1cc" />
<img width="1887" height="863" alt="Screenshot 2026-02-09 222737" src="https://github.com/user-attachments/assets/dfa876cb-25db-4c15-a7a7-cc90a30020b8" />
<img width="1884" height="879" alt="Screenshot 2026-02-09 222730" src="https://github.com/user-attachments/assets/80c3e868-2334-4483-a470-d4bda9b983e1" />







