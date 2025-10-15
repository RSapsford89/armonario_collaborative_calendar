from django.db import models

# Create your models here.
#needs @isAuth signal on the view so that the user profile info can be used to populate some fields
class GroupProfile():
    GroupName = models.CharField(blank=False max_length=128)
    GroupOwner = #This needs to link to the table of the user... Either Junction table or not?
    GroupColour = models.CharField(blank=False, default='FFFFFF', max_length=6) #hex colour value, should link to color icker hex on the html side
    GroupShareCode = models.CharField(blank=False, max_length=12)#a random 12 character share code, generated when creating at the form?

    def __str__(self):
        return self.GroupName
