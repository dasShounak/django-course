# Django

## 13/ Relative URLs

---

### 13.1 Using relative URLs

Generally, we use URLs in the HTML pages in Django like this:

```html
<a href="basic_app/page.html">LINK TO PAGE</a>
```

But, we can instead use template tagging to use relative URLs instead. This prevents hard coding absolute paths in every HTML file.

```html
<a href="{% url 'basic_app:page' %}"></a>
<a href="{% url 'admin:index' %}"></a>
```

Make sure to include `app_name=‘basic_app’` in application’s `urls.py`. `app_name` is a global variable and Django automatically detects it. It basically defines the application namespace. Always use this when using template tagging

```py
from django.urls import path
from . import views

app_name = 'basic_app'		# FOR TEMPLATE TAGGING

urlpatterns = [
	path('other/',views.other,name='other'),
	path('relative/',views.relative,name='relative'),
]
```

