from django.shortcuts import render, redirect
from django.http import HttpResponse
from Category.models import Category
from Category.forms import FormCategory
from datetime import datetime

# Create your views here.
def index(request):
    #return HttpResponse("<h1>This is Category Page</h1>")
    ## Demo session
    num_visit_session =  request.session.get('visit_session', 0)
    request.session["visit_session"] = num_visit_session + 1

    lsCategories = Category.objects.all()
    response = render(request, "Category/index.html", context = {"lsCategories" : lsCategories, "count": 0, "count_visit": num_visit_session})
    ## Demo cookies
    response.set_cookie("last_visit", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    return response

def get_all_categories(request):
    return HttpResponse("<h2>This is GetAll Categories</h2>")

def detail(request, id=2):
    return HttpResponse(id)

# Create your views here.  
def create(request):
    value_ck = request.COOKIES.get("last_visit")
    text_ck = "<h2>The lastest time I come here %s</h2>" + value_ck
    visit_session = request.session.get("visit_session",0)
    if request.method == "POST":  
        form = FormCategory(request.POST, request.FILES)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/categories')  
            except:  
                pass  
    else:  
        form = FormCategory()
    return render(request,'Category/create.html',{'form':form, "text_ck": text_ck, "visit_session" : visit_session})