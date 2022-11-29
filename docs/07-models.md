# Django

## 7/ Models

---

### 7.1 Models and Databases

We use Models to incorporate a database into a Django Project. Django comes equipped with SQLite. But it can connect to a variety of SQL engine backends.

In the `settings.py` file you can edit the ENGINE parameter used for DATABASES

### 7.2 Creating Models

1. We use a class structure inside of the relevant applications `models.py` file

   This class object is a subclass of `django.db.models.Model` built-in class. Each attribute of a class represents a field, just like a column name with constraints in SQL.

   To create a model, open the `models.py` file in your project directory.

   ```python
   class Topic(models.Model):
       top_name = models.CharField(max_length=264, unique=True)
   
   class Webpage(models.Model):
       category = models.ForeignKey(Topic, on_delete=models.CASCADE)
       name = models.CharField(max_length=264)
       url = models.URLField()
       
       def __str__(self):
           return self.name
   
   class AccessRecord(models.Model):
       name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
       date = models.DateField()
   
       def __str__(self):
           return str(self.date)
   ```

2. After creating the models, we need to migrate the database. Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

   ```bash
   python manage.py migrate
   ```

   Now, we need to register the changes to the application

   ```bash
   python manage.py makemigrations first_app
   ```

   Then, migrate the database one more time using the `migrate` command.

3. In order to use the admin interface with models, we need to register them to the `admin.py` file.

   ```python
   from django.contrib import admin
   from first_app.models import Topic, Webpage, AccessRecord
   
   # Register your models here.
   admin.site.register(AccessRecord)
   admin.site.register(Webpage)
   admin.site.register(Topic)
   ```

   Now, to login to the admin interface, we need to create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

   Provide name, email, and a password

4. Run the server and head over to https://127.0.0.1:8000/admin. From here you can login to Django Administrator.
