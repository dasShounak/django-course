# Django

## 4/ URL Mapping

---

### 4.1 Why Use include()

Previously, we imported our application directly into the project to map `views.py` to `urls.py`.  Now we will use the **`include()`** function from `django.urls` module.

The `include()` function allows referencing other URLconfs (i.e. other `urls.py` files, in this case the application’s own `urls.py` file). 

The idea behind `include()` is to make it easy to plug-and-play URLs. Since first_app is in its own URLconf (`first_app/urls.py`), it can be placed under `“/first_app/”`, or under “/foobar/”, or under `“/content/first_app/”`, or any other path root, and the app will still work.

### 4.2 Using django.urls.include()

1. First we need to create a new `urls.py` file inside our applications directory.

   ```bash
   cd /my_project/first_app
   touch urls.py
   ```

2. Add these lines to the newly created file:

   ```python
   # ./first_app/urls.py
   
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```

3.  Okay, so now we have mapped `views.py` to the application’s own `urls.py`. Next, we need to simply include this `urls.py` into the project’s `urls.py`

   ```python
   # ./my_project/urls.py
   
   from django.contrib import admin
   from django.urls import path, include
   # from first_app import views 	<------ previous direct method
   
   urlpatterns = [
       path('first_app/', include('first_app.urls')),		# Can put any directory name in place of first_app
       # path('', views.index, name='index'), 	<--- previous direct method 
       path('admin/', admin.site.urls),
   ]
   ```

4. Now,  run the server to see the changes. This time, we need to navigate to `http://127.0.0.1:8000/first_app/` to view the changes. We can change the path to anything in the project’s URLconf.
