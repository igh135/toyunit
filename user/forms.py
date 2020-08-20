from django import forms
from user.models import User  # 1


class UserForm(forms.ModelForm):
    class Meta:  # 2
        model = User
        fields = ['UserID', 'password', 'name']
