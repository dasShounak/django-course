from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
	return render(request,'forms_app/index.html')

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
