# Django

## 3/ Django Applications and Creating Views

---

### 3.1 Projects vs Applications

An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

> Django applications can be plugged into other Django projects, so they can be reused. So you can use other people’s applications.

### 3.2 Creating Django Application

1. To create a Django application, change into the outer `my_project` directory and type:

   ```bash
   python manage.py startapp first_app
   ```

   This will create a new directory named first_app inside the outer my_project directory. It should look like this:

   ```bash
   first_app
   │   ├── migrations
   │   │   ├── __init__.py
   │   ├── admin.py
   │   ├── apps.py
   │   ├── __init__.py
   │   ├── models.py
   │   ├── tests.py
   │   └── views.p
   ```

2. Next, open `my_project/settings.py` and add first_app to the `INSTALLED APPS` list.

   ```python
   # Application definition
   
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'first_app', 	# <------------------------ ADD THIS LINE
   ]
   ```

3. Now, its time to create a view. Open `first_project/views.py` file. Django views are Python functions that takes *http requests* and returns *http response*, like HTML documents.

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   
   # Create your views here.
   def index(request):
   	return HttpResponse("Hello World")
   ```

   > **Note:** To send a HTTP Response, we need to import the `HttpResponse` method from `django.http` module.

4. Next, in order to see the response in our web app,  we need to add a path to the view in `my_project/urls.py` file.

   ```python
   path('', views.index, name = 'index')
   ```

   ```python
   from django.contrib import admin
   from django.urls import path
   from first_app import views		# Import views from the application
   
   urlpatterns = [
       path('', views.index, name = 'index'),	# Add the path to your view before 'admin/'
       path('admin/', admin.site.urls),
   ]
   ```

5. Start the web server and see the results

   ```bash
   python manage.py runserver
   ```

   