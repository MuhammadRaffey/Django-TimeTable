
# Django Timetable Project

This is a Django project for managing timetables. It allows users to create, view, edit, and delete timetables for various purposes.

## Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/MuhammadRaffey/Django-TimeTable
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment (optional but recommended)
python3 -m venv .venv

# Activate virtual environment for Linux/Mac 
source .venv/bin/activate

# Activate virtual environment for Windows
.venv/Scripts/activate 
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Perform Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account which you can use to access the Django admin interface.

### 6. Run the Development Server

```bash
#To run you must be in the manage.py file directory
python manage.py runserver
```
The development server will start running at `http://127.0.0.1:8000/`. You can access the project by visiting this URL in your web browser.

## Usage

- **Admin Interface**: Access the Django admin interface by visiting `http://127.0.0.1:8000/admin/`. Log in using the superuser credentials created earlier. Here you can manage users, timetables, and other site content.
- **Frontend Interface**: If applicable, there may be a frontend interface for interacting with timetables. Access this interface through the project's main URL (`http://127.0.0.1:8000/`).

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request with your changes. Make sure to follow the project's coding standards and guidelines.

