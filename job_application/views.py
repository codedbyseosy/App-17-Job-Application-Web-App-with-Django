from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form # importing the class that creates the database in the 'model.py' folder
from django.contrib import messages # messages is a django method that allows you to display messages on the webpage
from django.core.mail import EmailMessage # 'EmailMessage' is a class we are importing

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST) # instantiated the application form class that we imported from 'forms.py'
        if form.is_valid(): # validate the form
            first_name = form.cleaned_data["first_name"] # extract user value 'first_name' out of the 'form' instance
            last_name = form.cleaned_data["last_name"] # extract user value 'last_name' out of the 'form' instance
            email = form.cleaned_data["email"] # extract user value 'email' out of the 'form' instance
            date = form.cleaned_data["date"] # extract user value 'date' out of the 'form' instance
            occupation = form.cleaned_data["occupation"] # extract user value 'occupation' out of the 'form' instance
            
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            
            message_body = f"""
                Thank you for your submission, {first_name}.
                Here are your data:
                Name: {first_name} {last_name}
                Occupation: {occupation}
                Thank you.
                """
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")