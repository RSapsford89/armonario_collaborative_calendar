from django.db import models
from django.contrib.auth.models import AbstractUser
from group_profile.models import GroupProfile

# Create your models here.
STATUS =((0,'none'),(1,'Owner'),(2,'Member'))#example found in CI Django walkthrough
class CustomUser(AbstractUser):
    """
    CustomUser extends/builds upon the base User
    model so that custom fields can be added
    """
    #Custom user fields follow here and should not
    #be the same as existing User.<object> fields
    #should also be blank=True to not break auth

    location = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField( max_length=50, blank=True)
    date_joined = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.username
    

class UserGroupLink():
    """
    Joining or Through table. This links the many to many fields of
    Group and Users through their IDs. Many Users can be in many groups
    and vice versa. 'status' used to denote the User as member/none/owner
    """
    customUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    groupProfile = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['customUser', 'groupProfile'], 
                name='unique_customUser_groupProfile'
            )
        ]