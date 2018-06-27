from django import forms
from django.contrib.auth import(
authenticate,
get_user_model
)
from proapp.models import Profile,Text

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            print(user)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    Conform_Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'Conform_Password',

        ]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'Email',
            'FatherName',
            'DateofBirth',
            'age',
            'address',
            'image'
        ]
    def clean_name(self):
        title = self.cleaned_data.get("title")
        if title == "Hello":
            raise forms.ValidationError("Not a valid name")
        return title

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = [
            'to',
            'text',

        ]
    def clean_name(self):
        title = self.cleaned_data.get("title")
        if title == "Hello":
            raise forms.ValidationError("Not a valid name")
        return title
