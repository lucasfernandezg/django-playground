from django.shortcuts import render
from users_page.models import Users
from users_page.forms import UsersForm

# Create your views here.
def users(request):
    users_list = Users.objects.order_by("first_name")
    users_dict = {"users_list":users_list}
    return render(request,"users_page/users.html",context=users_dict)

def index(request):
    return render(request,"users_page/index.html")

def form_view(request):
    form = UsersForm()
    form_dict = {"form":form}

    if request.method == "POST":
        form = UsersForm(request.POST)

        if form.is_valid():
            form.save()
            print("Validation Success")
            return index(request)
        else:
            print("Error from invalid data")

    return render(request,"users_page/users_form.html",context=form_dict)
