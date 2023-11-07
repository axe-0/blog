# Django Blog application

This is a django blog and ploss application.

## Running the Application

### Using venv

1. Clone the repository:
   ```bash
   git clone https://github.com/axe-0/blog.git

1.1 Create a virtual environment (if not already created):

      A) use pipn ormally when installing packages

            > python -m pip install pip

      B) nstall package to enable virtual envirment 

                > pip install virtualenv

1.2 Activate the virtual environment:
  On macOS and Linux:
    
      source venv/bin/activate

  On Windows:

    .\venv\Scripts\activate


1.3 Navigate into hyperion/ and Install project dependencies:

    pip install -r requirements.txt
    
1.4 Run the development server:

    python manage.py runserver
    
1.5 Access the application in your web browser at http://localhost:8000/

### Using Docker 

2.1 Clone the repository:

    git clone https://github.com/axe-0/blog.git

2.2 Build the Docker image:

    docker build -t django-blog-app .

  Substitute 'django-blog-app' with your preferred name.
    
2.3 Run the Docker container:

    docker build -t django-blog-app .

  use the name set above for the app 

2.4 Access the application in your web browser at http://localhost:8000/

### Security Keys 

  security configurations for this application can be found in the 'security_config.txt' file in the dropbox

### License


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

For the full text of the MIT License, please visit [opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).
