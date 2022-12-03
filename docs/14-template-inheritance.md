# Django

## 14/ Template Inheritance

---

### 14.1 Importance of Inheritance

Template inheritance is used to implement DRY concept. For example, a website generally has the same navbar on all the pages. So, instead of copying the same HTML code in every HTML file, we can instead create a single template and reuse it in every page.

### 14.2 Creating a Template

1. Create a new HTML file inside the `template/application_name/` directory. Let’s name it `base.html`.

   ```django
   <!DOCTYPE html>
   <html lang="en">
   <head>
   	<meta charset="UTF-8">
   	<meta name="viewport" content="width=device-width, initial-scale=1.0">
   	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
   	<title>
   		{% block title %}
   		{% endblock %}
   	</title>
   </head>
   <body>
   	<nav class="navbar navbar-expand-lg bg-light">
   		<div class="container-fluid">
   			<a href="{% url 'index' %}" class="navbar-brand">Brand</a>
   			<ul class="navbar-nav me-auto">
   				<li class="nav-item">
   					<a href="{% url 'basic_app:other' %}" class="nav-link">Other</a>
   				</li>
   				<li class="nav-item">
   					<a href="{% url 'basic_app:relative' %}" class="nav-link">Relative URLs</a>
   				</li>
   				<li class="nav-item">
   					<a href="{% url 'admin:index' %}" class="nav-link">Admin</a>
   				</li>
   			</ul>
   		</div>
   	</nav>
   
   	<div class="container">
   		{% block body %}
   		{% endblock %}
   	</div>
   
   </body>
   </html>
   ```

   The `{% block block_name %}` is where the page specific contents will be placed.

2. Now open the other HTML file that will inherit this template. Add all the page specific content inside the template block tags.

   ```django
   <!DOCTYPE html>
   {% extends "basic_app/base.html" %}
   {% block title %}
   Other
   {% endblock %}
   
   {% block body %}
   <h1 class="display-2">Welcome to Other</h1>
   {% endblock %}
   ```

   > `<!DOCTYPE html>` must be there in the first line.