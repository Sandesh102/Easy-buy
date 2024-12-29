Ecommerce App Setup Guide
Clone the Repository

To get started, clone the repository to your local machine:
git clone https://github.com/XDezoTech/ecommerce-app.git
cd ecommerce-app
Install Python Dependencies
[asgiref==3.8.1
colorama==0.4.6
Django==5.1.4
mysqlclient==2.2.6
pillow==11.0.0
qrcode==8.0
sqlparse==0.5.3
tzdata==2024.2
]
If you encounter an issue with pip not being found, ensure that Python is added to your system PATH.



Create and Activate a Virtual Environment

For Linux/macOS:
python3 -m venv venv
source venv/bin/activate


For Windows:
python -m venv venv
venv\Scripts\activate



MySQL Configuration (Default)

To use MySQL, update the DATABASES settings in settings.py with your credentials:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',  # Replace with your MySQL database name
        'USER': 'your_mysql_user',  # Replace with your MySQL username
        'PASSWORD': 'your_mysql_password',  # Replace with your MySQL password
        'HOST': 'localhost',  # Keep as localhost or replace with your MySQL host if remote
        'PORT': '3306',  # Default MySQL port
    }
}
SQLite Configuration (If using SQLite)

If you want to switch to SQLite, update DATABASES in settings.py like this:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Set Up the Application

TO import data ,run following command
  python manage.py loaddata data.json

Apply Database Migrations

Run the following command to apply migrations and set up the database:

python manage.py migrate
Create a Superuser

To access the Django admin panel, create a superuser by running:

python manage.py createsuperuser
Follow the prompts to set up the superuser credentials.

Run the Development Server

Start the Django development server:

python manage.py runserver
You can now access the application at http://127.0.0.1:8000.

