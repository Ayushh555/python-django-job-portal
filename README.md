# 💼 Online Job Portal

A full-stack **Online Job Portal** built with **Python and Django** that connects job seekers with employers. Job seekers can browse and apply for jobs, while HR users can post job openings and manage applications through their dashboard.

## 🚀 Live Demo

**Live Website:**
https://python-django-job-portal.onrender.com

---

## 📌 About the Project

The **Online Job Portal** provides a simple platform for two types of users:

* 👨‍💻 **Job Seekers** — Create an account, browse available jobs, and apply for suitable positions.
* 🧑‍💼 **HR / Employers** — Create an account, post job openings, view applications, and shortlist candidates.

The project also includes an **Admin Panel** for managing the overall application and its data.

---

## ✨ Features

### 👨‍💻 Job Seeker

* User registration and login
* Browse available job listings
* View job details
* Apply for jobs
* Manage job applications
* Track submitted applications

### 🧑‍💼 HR / Employer

* HR registration and login
* Post new job vacancies
* Manage posted jobs
* View applications received
* Review candidate information
* Shortlist candidates

### 🔐 Authentication

* User registration
* Secure login/logout
* Role-based access
* Separate functionality for Job Seekers and HR users

### 🛠️ Admin Panel

* Manage users
* Manage jobs
* Manage applications
* Overall control of the platform

---

## 🏗️ Project Structure

```text
Online-Job-Portal/
│
├── manage.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── jobs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── templates/
│
├── static/
│
├── requirements.txt
│
└── README.md
```

> Adjust the folder names above if your actual repository uses different Django app names.

---

## 🛠️ Technologies Used

| Technology            | Purpose               |
| --------------------- | --------------------- |
| 🐍 Python             | Backend programming   |
| 🌐 Django             | Web framework         |
| 🗄️ SQLite / Database | Data storage          |
| HTML5                 | Website structure     |
| CSS3                  | Styling               |
| JavaScript            | Frontend interactions |
| Bootstrap             | Responsive UI         |
| Git & GitHub          | Version control       |
| Render                | Deployment            |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the Project

```bash
cd Online-Job-Portal
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the instructions to create your admin account.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔄 How It Works

```text
                 ONLINE JOB PORTAL
                         │
          ┌──────────────┴──────────────┐
          │                             │
     👨‍💻 JOB SEEKER                 🧑‍💼 HR
          │                             │
       Register                      Register
          │                             │
        Login                         Login
          │                             │
    Browse Jobs                  Post Jobs
          │                             │
    View Details                Manage Jobs
          │                             │
      Apply Job                View Applications
          │                             │
          └──────────────┬──────────────┘
                         │
                   🛠️ ADMIN PANEL
                         │
                  Manage Platform
```

---

## 🎯 Main Objectives

* Provide an easy-to-use platform for job seekers and employers.
* Simplify the job searching and application process.
* Allow HR users to manage job vacancies and candidates.
* Implement role-based authentication and authorization.
* Provide centralized administration through Django Admin.
* Build and deploy a real-world Django web application.

---

## 🔮 Future Improvements

Some features that can be added in future versions:

* 🔎 Advanced job search and filtering
* 📍 Location-based job search
* 📄 Resume upload
* 📧 Email notifications
* 💬 Employer–candidate messaging
* ⭐ Candidate profiles
* 🔔 Job alerts
* 📊 HR analytics dashboard
* 🔐 Additional security improvements

---

## 👨‍💻 Developer

**Ayush Chandel**

**Software Developer | Python & Django**

* GitHub: https://github.com/Ayushh555
* LinkedIn: https://www.linkedin.com/in/ayush-chandel-a2b726252/

---



