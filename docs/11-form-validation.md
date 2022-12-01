# Django

## 11/ Form Validation

---

### 11.1 Checking for POST request

In the `views.py`, we can check for POST requests.

Firstly, check if there’s a POST request made by the form submission. If a POST request is made, return it to the form object::

```py
if request.method == 'POST':
    form = forms.SampleForm(request.POST)
    # do something
```

If a POST request is made, return it to the form object:

```py
form = forms.SampleForm(request.POST)
```

We can also return the cleaned data, ie, validated data, to the console:

```py
if form.is_valid():
			print("VALIDATION SUCCESS")
			print("NAME: "+form.cleaned_data['name'])
			print("EMAIL: "+form.cleaned_data['email'])
			print("MESSAGE: "+form.cleaned_data['message'])
```

The final code should look like:

```py
def form_view(request):
	form = forms.SampleForm()

	if request.method == 'POST':
		form = forms.SampleForm(request.POST)

		if form.is_valid():
			print("VALIDATION SUCCESS")
			print("NAME: "+form.cleaned_data['name'])
			print("EMAIL: "+form.cleaned_data['email'])
			print("MESSAGE: "+form.cleaned_data['message'])

	return render(request,'forms_app/form.html',{'form':form})
```

### 11.2 Using a hidden botcatcher field

We can create a hidden text field and check if its empty on submission. Only a bot will put some value in it. So we can just check the length of that input field. For this, we use Django’a `clean_field()`  function. The `field` part should be the name of the input field. `clean_` is a prebuilt method in Django, it scans for any function starting with `clean_` for validation purposes.

```py
botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)

	def clean_botcatcher(self):
		botcatcher = self.cleaned_data['botcatcher']
		if len(botcatcher) > 0:
			raise forms.ValidationError("Gotcha bot!")
```

### 11.3 Using Built-in Validators

There are few built-in validators which can be used in most cases.

```py
from django.core import validators

botcatcher = forms.CharField(required=False,
								 widget=forms.HiddenInput,
								 validators=[validators.MaxLengthValidator(0)])
```

The `MaxLengthValidator` checks for maximum length of the input value and compares it to the value passed to it as an argument.

We can use more than one validators on a single field.

### 11.4 Custom Validation Function

If there isn’t a built-in validator for checking something we can define our own function.

Suppose we need to check if the first letter of name is equal to `S`.

```py
def check_for_s(value):
	if value[0].lower() != 's':
		raise forms.ValidationError("Name must start with 'S'")

class SampleForm(forms.Form):
	name = forms.CharField(validators=[check_for_s])
```

> The argument name of the function must be `value` so that Django knows it is used for validation of user input in the field.

### 11.5 Comparing values of two fields (Email/Password verification)

We can use the `clean` method to check of the user input of two separate fields is same or not. This comes handy in email/password verification.

```py
class SampleForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	verify_email = forms.EmailField(label='Enter your email again')
	message = forms.CharField(widget=forms.Textarea)

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']

		if email != vmail:
			raise forms.ValidationError("Email addresses do not match!")
```

> The `clean()` method is used to clean the entire form while the `clean_` methods are for cleaning a single field.