from django.db import models
from user_profile.models import CustomUser
from datetime import date


# Create your models here.
def todays_date():
    today = date.today()
    return today


class Event(models.Model):
    """
    Event model to contain all fields associated
    with the calendar Events. PrivateEvent for later
    use in later releases. EventCreatedTime is for Admin
    use in case of User issues.
    """
    EventName = models.CharField(blank=False, max_length=128)
    PrivateEvent = models.BooleanField(blank=False, default=True)
    # for later releases where displays could be 'your profile'
    #  but you don't want it to show the event
    group = models.ForeignKey(
        'group_profile.GroupProfile',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='events'
    )
    StartDate = models.DateField(blank=False, default=todays_date)
    EndDate = models.DateField(blank=False, default=todays_date)
    StartTime = models.TimeField(blank=False)
    EndTime = models.TimeField(blank=False)
    Location = models.CharField(blank=True, default="Enter a place")
    Notes = models.TextField(blank=True, )
    EventCreatedTime = models.DateTimeField(auto_now_add=True)  # for Admin purposes

    def __str__(self):
        return self.EventName


STATUS = (
    (0, 'none'), (1, 'owner'), (2, 'invited'), (3, 'accepted'), (4, 'declined')
    )


class UserEventLink(models.Model):
    """
    Joining table. Links Many to Many field of
    User to Events: Many Users can be in Events
    and vice versa. 'status' for none/owner/accepted/
    invited/declined
    """
    customUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['customUser', 'event'],
                name='unique_customUser_event'
            )
        ]
