# Django

## 12/ Creating Forms from Models

---

So far, we have only returned user data to the console. But in real websites, we need to store that data in the database. To do that, Django has Model Forms.

### 12.1 Creating Model Forms

1. To create model form, we need a model first. Let’s say we have a users model.

   ```py
   class User(models.Model):
       first_name = models.CharField(max_length=128)
       last_name = models.CharField(max_length=128)
       email = models.EmailField(max_length=254,unique=True)
   
       def __str__(self):
           return self.email
   ```

2. Now, create a new form in `forms.py` file inside the application folder. We need to import the model since the form fields will be generated directly from the model.

   ```py
   from django import forms
   from appTwo.models import User
   
   class UserRegisterForm(forms.ModelForm):
       # We can optionally create the fields here
       # Especially when we have to use validators
   	class Meta:
   		model = User
   		fields = "__all__"
   ```

   The child class `Meta` specifies the model, the fields to be generated from that model, etc.

   * **model:** The model from which the form is to be generated.
   * **fields:** The model attributes which will generate a form field. It as three options:
     			1. `"__all__"`: Include all attributes
     			1. `include(field1, field2, ...)`: Include only specified fields
     			1. `exclued(field1, field2, ...)`: Exclude only specified fields

3. Now create a template and view.

4. We need to save the validated form input to the database. So, in the `views.py` we need to use a function `save()` to save the form data into the model.

   ```py
   from django.shortcuts import render
   from . import forms
   
   def form(request):
       form = forms.UserRegisterForm()
   
       if request.method == 'POST':
           form = forms.UserRegisterForm(request.POST)
   
           if form.is_valid():
               form.save()
               return index(request)
           else:
               print('ERROR: Form Invalid')
   
       return render(request,'appTwo/users.html',context={'form':form})
   ```

   
