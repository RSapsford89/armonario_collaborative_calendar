from django import forms
from group_profile.models import GroupProfile

class GroupForm(forms.ModelForm):
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