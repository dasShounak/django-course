# Django

## 10/ Forms

---

### 10.1 Creating forms

1. Create a `forms.py` file inside the application directory, similar to models.

   ```py
   from django import forms
   
   class SampleForm(forms.Form):
   	name = forms.CharField()
   	email = forms.EmailField()
   	message = forms.CharField(widget=forms.Textarea)
   ```

   > For **textarea**, we use a `CharField` object and pass a `widget` argument `forms.textarea`

2. Now, we need to create a view to display the form

   ```py
   from . import forms
   
   def form_view(request):
   	form = forms.SampleForm()
   	return render(request,'forms_app/form.html',{'form':form})
   ```

3. Inside templates directory, create an HTML file `forms.html`

   ```django
   <!DOCTYPE html>
   <html lang="en">
   <head>
   	<meta charset="UTF-8">
   	<meta name="viewport" content="width=device-width, initial-scale=1.0">
   	<title>Form</title>
   </head>
   <body>
   	<h1>Fill out the form!</h1>
       <form method="POST">
           {{ form.as_p }}
           {% csrf_token %}
           <input type="submit" class="btn btn-primary" value="Submit">
       </form>
   </body>
   </html>
   ```

   `form.as_p` will render the form elements as paragraphs. Otherwise all input fields will be in a single line.

   > #### Important:
   >
   > The `csrf_token` is required by Django as a security measure. CSRF stands for Cross-Site Request Forgery