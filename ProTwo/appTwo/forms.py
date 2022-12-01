from django import forms
from appTwo.models import User

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = "__all__"
		labels = {
			'first_name': 'First Name',
			'last_name': 'Last Name',
			'email': 'Email'
		}

	def __init__(self, *args, **kwargs):
	    super(UserRegisterForm, self).__init__(*args, **kwargs)
	    for field in self.fields:
	    	self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'