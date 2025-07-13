# Product Review System - Django REST API

This is a Django-based RESTful API for a **Product Review System** where:

- **Admin users** can manage (add/edit/delete) products.
- **Regular users** can browse products and submit reviews.
- **All users** can view product details and aggregated ratings.

---

## Features

- User registration & login with token authentication
- Role-based access control (admin vs regular users)
- Product catalog with average ratings
- Review system (one review per user per product)
- RESTful API built with Django REST Framework

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <https://github.com/Haripranav-RG/product_review_system>
cd product_review_system
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

### 6. Run the server

```bash
python manage.py runserver
```

The API will now be running at `http://127.0.0.1:8000/`



