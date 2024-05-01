from django.shortcuts import render
from .forms import ApplicationForm

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST) # instantiated the application form class that we imported from 'forms.py'
        if form.is_valid(): # validate the form
            first_name = form.cleaned_data["first_name"] # extract user value 'first_name' out of the 'form' instance
            last_name = form.cleaned_data["last_name"] # extract user value 'last_name' out of the 'form' instance
            email = form.cleaned_data["email"] # extract user value 'email' out of the 'form' instance
            date = form.cleaned_data["date"] # extract user value 'date' out of the 'form' instance
            occupation = form.cleaned_data["occupation"] # extract user value 'occupation' out of the 'form' instance
            print(first_name)
    return render(request, "index.html")