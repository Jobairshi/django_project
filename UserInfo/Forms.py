from django import forms
from .models import userInfo

class userForm(forms.ModelForm):
    class Meta:
        model = userInfo
        fields = [
            'user_name',
            'user_email',
            'user_pass',
            'user_phone'
        ]
