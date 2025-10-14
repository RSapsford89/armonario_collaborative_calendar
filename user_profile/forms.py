from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm 
from django import forms 
User = get_user_model()

class CustomUserForm(UserCreationForm):
    """
    UserCreationForm is bound to the AUTH_USER_MODEL string
    This stops the form Meta.model from using default auth.User
    instead of this one
    """

    email = forms.EmailField()
    first_name = forms.CharField( max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name','last_name', 'location', 'phone_number','email','password1','password2')