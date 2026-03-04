# Django-Custom-User-Authentication-System

# CustomAuth Blog System

[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-green)](https://www.djangoproject.com/)


## 🚀 Project Overview
CustomAuth Blog System is a **Django web application** that combines a **custom authentication system** with a fully functional blog platform.  
Users can **register, login, create, edit, and delete blogs** while enforcing proper access control and permissions.

### Key Features
- **Custom User Model** using `AbstractBaseUser` and `PermissionsMixin`
- Email-based login
- Registration with password confirmation
- Protected dashboard and user profile
- Blog management: create, edit, delete (only by author)
- Public blog list and detail pages for all visitors
- Draft and Published blog statuses
- Guest access (view-only) & logged-in user access

---

## 🖥 Pages / Functionality
| Page | Access |
|------|--------|
| Blog List | Everyone |
| Blog Detail | Everyone |
| Create Blog | Logged-in Users only |
| Edit / Delete Blog | Only author |
| User Profile | Only logged-in users |

---

## ⚡ Technologies Used
- **Django 6.0**
- **Python 3.14**
- **SQLite** (default DB, can be changed)
- HTML / CSS / Bootstrap (optional)

---

## 📂 Installation & Run
1. Clone the repo:

Create virtual environment & install dependencies:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Create superuser:

python manage.py createsuperuser

Run server:

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser






