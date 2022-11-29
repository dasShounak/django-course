# Django

## 6/ Working with Static Files

---

### 6.1 Inserting Static Files

Templates are not only used to insert plain HTML text. We need to insert static media files, CSS, and JavaScript too.

1. To do so, first create a new directory in the project root just like templates

   ```bash
   # Inside /my_project
   mkdir static
   ```

   Inside this, create another folder for images

   ```bash
   mkdir static/images
   ```

   Store all your images in this folder.

2. Now we need to add this directory path to the project’s `settings.py` file.

   ```python
   STATIC_DIR = BASE_DIR / 'static'
   ```

   Also, scroll down to the bottom to find `STATIC_URL` variable. If not present by default, create it.

   ```python
   STATIC_URL = 'static/'
   ```

   When building a Django project, you might have multiple applications with their own static files stored in a dedicated directory. So, in addition the `STATIC_DIR` we can store the list of such directories in another variable to allow Django to look for static files in there.

   ```python
   STATIC_URL = 'static/'
   STATICFILES_DIRS = [
       STATIC_DIR,
       'var/www/static',
       .
       .
       .
   ]
   ```

3. Open `index.html` and add a line just after `<!DOCTYPE html>` to indicate Django that we are including static files.

   ```django
   <!DOCTYPE html>
   {% load static %}
   ```

   This is the syntax of Django **tags**. Variables use double braces (`{{ }}`) while tags use a braces and percentage (`{% %}`).

4. Add an `<img>` tag to include the image in static folder. In the *src* atrribute, add a tag that looks like this:

   ```django
   {% static 'images/3.jpg' %}
   ```

   ```django
   <img src="{% static 'images/3.jpg' %}" alt="oops! can't dislpay image!" />
   ```

   > **Note:** The tag should be enclosed in quotes

5. Run the server to see the changes