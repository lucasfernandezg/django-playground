from django import forms
from users_page.models import Users

class UsersForm(forms.ModelForm):
    class Meta():
        model = Users
        fields = "__all__"  #("","",...) or instead of fields you code exclude = ["","",...]
