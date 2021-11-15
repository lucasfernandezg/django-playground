from django.conf.urls import url
from users_page import views

#TEMPLATE TAGGING
app_name = "users_page"

urlpatterns = [
    url(r"^users/$",views.users,name="users"),
    url(r"^$",views.index,name="index"),
    url(r"^form/$",views.form_view,name="usersform"),
]
