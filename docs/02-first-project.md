# Django

## 2/ Creating Django Projects

---

### 2.1 Installing Django

You can install django with:

* `conda install django`

  OR

* `pip install django`

Django comes with a command line tool `django-admin`. To create a project, first make a new directory:

```bash
mkdir django-project
cd django-project
```

Then, activate the django environment:

```bash
conda activate djangoDev
```

To create a project, type:

```bash
django-admin startproject my_project
```

It will create a new directory name “my_project” with another directory of the same name nested inside.

```
── my_project
    ├── manage.py
    └── my_project
        ├── asgi.py
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

* `manage.py`: A command-line utility that lets you interact with this Django project in various ways.
* The inner `mysite/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `mysite.urls`).
* `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
* `settings.py`: Settings/configuration for this Django project.
* `urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
* `asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. ASGI stands for Asynchronous Server Gateway Interface.
* `wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. WSGI stands for Web Server Gateway Interface.

### 2.2 Running Django server

To verify if the Django project works, change into the outer my_project directory and run:

```bash
python manage.py runserver
# OR to specify different port (default 8000)
python manage.py runserver 8000
# OR to specify IP and port (default 127.0.0.1:8000)
python manage.py runserver 0.0.0.0:8000
```

> **Automatic reloading of `runserver`**
>
> The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like *adding files* don’t trigger a restart, so you’ll have to restart the server in these cases.
