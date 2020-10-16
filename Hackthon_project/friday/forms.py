from django.contrib.auth import get_user_model
from django import forms
from .choices import designation_choices
from .models import UserProfileInfo

class UserCreateForm(forms.ModelForm):
    cpassword = forms.CharField(max_length=100)
    class Meta():
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        model = get_user_model()

        widgets = { 
            'first_name':forms.TextInput(attrs={'class': 'input-login'}),
            'last_name':forms.TextInput(attrs={'class': 'input-login'}),
            'username':forms.TextInput(attrs={'class': 'input-login'}),
            'email':forms.TextInput(attrs={'class': 'input-login'}),
            'password':forms.PasswordInput(attrs={'class': 'input-login'}),
            'cpassword':forms.PasswordInput(attrs={'class': 'input-login'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Employee ID'

        for fieldname in ['first_name', 'last_name', 'username', 'email', 'password']:
            self.fields[fieldname].help_text = None


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo

        fields = [
            'date_of_birth',
            'res_address',
            'personal_contact_no',
            'emergency_contact_no',
            'personal_email',
            'designation',
            'salary',
            'passport_pic',
            'joining_date',
            ]

        widgets = {
            'res_address': forms.Textarea(attrs={'class':'input-login','row':'3','width': '100%'}),
            'personal_contact_no': forms.TextInput(attrs={'class': 'input-login'}),
            'emergency_contact_no': forms.TextInput(attrs={'class': 'input-login'}),
            'personal_email': forms.TextInput(attrs={'class': 'input-login'}),
            'designation': forms.Select(),
            'salary': forms.TextInput(attrs={'step':'10000'}),
        }