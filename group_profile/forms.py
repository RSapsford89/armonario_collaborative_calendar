from django import forms
from group_profile.models import GroupProfile

class CreateGroupForm(forms.ModelForm):
    """
    Form contents to render in the view
    for  creating Groups
    """

    class Meta():
        model = GroupProfile
        fields = (
            'GroupName',
            'GroupColour',
            'GroupShareCode'
            )
        widgets = {
            'GroupColour': forms.ColorInput(),
        }
        

class JoinGroupForm(forms.ModelForm):
    """
    Form contents to render in the view
    for Joining a Group.
    """

    class Meta():
        model = GroupProfile
        fields = (
            'GroupName',
            'GroupShareCode'
        )