Step 1: Clone the Repository(Only few members may have access to the repo so we cannot clone from every github account)
# Clone the repository to your local machine
git clone https://github.com/XDezoTech/ecommerce-app.git
cd ecommerce-app

Step 2: Install Python Dependencies

      Create and activate a virtual environment:
      
      Linux/macOS:
      
      python3 -m venv venv
      source venv/bin/activate
      
      Windows:
      
      python -m venv venv
      venv\Scripts\activate
      
      Install the required Python packages:
      
      pip install -r requirements.txt
      
      Note: If pip is not found, ensure Python is added to your system PATH.
      
      Install additional dependencies if needed:
      
      Linux/macOS:
      
      sudo apt-get install python3-dev libmysqlclient-dev
      pip install mysqlclient
      
      Windows:
      
      pip install mysqlclient
      
      Ensure Pillow is installed:
      Pillow is listed in requirements.txt and is installed with other dependencies. If it’s missing, install manually:
      
      pip install pillow

Step 3: Configure the Database

     Install the required Python packages:
     
     pip install -r requirements.txt
     
     Note: If pip is not found, ensure Python is added to your system PATH.
     
     Here are the key dependencies included in requirements.txt:
     
     Django: Web framework
     
     mysqlclient: MySQL database connector
     
     Pillow: For handling media files

Step 4: Set Up the Application

    Apply database migrations:
    
    python manage.py migrate
    
    Create a superuser to access the admin panel:
    
    python manage.py createsuperuser
    

Step 5: Run the Development Server

    Start the server using the following command:
    
    python manage.py runserver
    
    Access the application at http://127.0.0.1:8000.