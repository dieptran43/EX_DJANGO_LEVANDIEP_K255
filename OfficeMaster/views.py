from django.shortcuts import render
from django.http import HttpResponse
from OfficeMaster.models import Contact
from OfficeMaster.forms import FormContact

# Create your views here.
def index(request):
    return render(request, 'OfficeMaster/index.html')

def about(request):
    return render(request, 'OfficeMaster/about.html')

def contact(request):
    registered = False
    form = FormContact()    
    if request.method == "POST":
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()
            registered = True
        else:
            print(form.errors)

    return render(request, 'OfficeMaster/contact.html', {'contact_form': form, 'registered': registered})

def team(request):
    return render(request, 'OfficeMaster/team.html')

def blog(request):
    return render(request, 'OfficeMaster/blog.html')
