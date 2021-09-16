# django-demo
## Using this Demo
First, git clone and navigate inside the directory by running these commands:
```bash
git clone https://github.com/umd-python-cas/django-demo.git
cd django-demo
```
Then, install the dependencies:
```bash
pip install -r requirements.txt
```
Finally, run the django webserver locally.
```bash
./manage.py runserver
```
Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to view the app.
## Starting from Scratch
The following are instructions on how this template was made, so you can better understand how to integrate umd-cas-python into your project.
### Installation
First, install django and umd-python-cas, and start a new django project, by running these commands:
```bash
pip install django umd-python-cas
django-admin startproject django_client_demo
```
This will create a new folder called `django_client_demo` and initialize it with all the normal django template files.
### Sub-App
Navigate into that new project folder, set up the database, and create a sub-app called `cas`, by running these commands:
```bash
cd django_client_demo
./manage.py migrate
./manage.py startapp cas
```
This will create a sub-folder called `cas`, where we will put the code for authenticaion.
### Views and URLs
Create a file `cas/views.py` with the contents of [this file](cas/views.py).

Create a file `cas/urls.py` with the contents of [this file](cas/urls.py).

Replace `django_demo/urls.py` with the contents of [this file](django_demo/urls.py).
### Template
Create a templates folder.
```bash
mkdir templates
```
Create `templates/index.html` with the contents of [this file](templates/index.html).

To allow this templates folder to be detected, inside `django_client_demo/settings.py`, change the line that reads:
```python
'DIRS': [],
```
to be:
```python
'DIRS': [''],
```
### Run
Run the django webserver locally.
```bash
./manage.py runserver
```

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to view the app.
