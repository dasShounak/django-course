# Django

## 5/ Templates

---

### 5.1 What are Templates

A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

* Template contains static parts of an HTML page
* Template tags, which have their own special syntax (neither HTML nor Python), that allows us to inject dynamic content that views will produce

### 5.2 Creating a Template

1. To get started, we need to create a `templates` directory in the root (outer `my_project` folder).

   ```bash
   # Inside ./my_project
   mkdir templates
   ```

   Then create an `index.html` file inside a folder of the same name as the Django application, i.e., `first_app` within the `templates` directory.

   ```bash
   # Inside ./my_project/templates
   mkdir first_app
   cd first_app
   touch index.html
   ```

2. Add some HTML

   ```django
   <!DOCTYPE html>
   <html lang="en">
   <head>
   	<meta charset="UTF-8">
   	<meta name="viewport" content="width=device-width, initial-scale=1.0">
   	<title>Document</title>
   </head>
   <body>
   	<h1>This is a template from first_app/index.html</h1>
   	{{ insert_me }} <!-- THIS IS A TEMPLATE VARIABLE -->
   
   </body>
   </html>
   ```

   Here, `insert_me` is a Django template variable. It is used to render dynamic HTML content in its place.

3. Now, head over to `views.py` in the application folder and add this function:

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   
   # Create your views here.
   def index(request):
   	my_dict = {"insert_me": "This is from first_app/views.py"}
   	return render(request, 'first_app/index.html', context=my_dict)
   ```

   We created a dictionary `my_dict` which contains a key `insert_me` which is actually the template variable name. Basically, we will replace the template variable in `index.html` with this string.

   The string will get rendered as normal text in the HTML. To do that, we need to use the `render()` function from `django.shortcuts` module which is already imported by default.

   We pass three arguments in this case:

   1. `request`: The request object used to generate this response
   2. `template_name`: The string `“first_app/index.html”`. The full name of the template
   3. `context`(optional): A dictionary of values to added to the template. By default its an empty dictionary.

4. Finally, we need to specify the location of the `templates` directory in the `settings.py` file. To do that, create a new variable `TEMPLATE_DIR`.

   ```python
   BASE_DIR = Path(__file__).resolve().parent.parent
   TEMPLATE_DIR = BASE_DIR / 'templates'
   ```

   Now, add this variable in the `DIRS` list inside the `TEMPLATES` list in the same file

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [TEMPLATE_DIR,],
           .
           .
           .
   ```

   Run the web server to see it in effect.

   
