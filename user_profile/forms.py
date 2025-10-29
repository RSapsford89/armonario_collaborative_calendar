from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()
# This code is based largely on the custom form built in
# the YouTube video by Codemy.com: https://www.youtube.com/watch?v=HdrOcreAXKk&t=397s


class CustomUserForm(UserCreationForm):
    """
    UserCreationForm is bound to the AUTH_USER_MODEL string
    This stops the form Meta.model from using default auth.User
    instead of this one
    """
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'location',
                  'phone_number', 'email', 'password1', 'password2')


class CustomUserFormEdit(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'location', 'phone_number', 'email', 'picture')
        widgets = {
            'first_name': forms.TextInput(attrs={'maxlength': 50}),
            'last_name': forms.TextInput(attrs={'maxlength': 50}),
        }
