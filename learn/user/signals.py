from django.db.models.signals import post_save#signal that gets fired everytime object is saved.
from django.contrib.auth.models import User#it is the sender as it sends the signal.
from django.dispatch import receiver#it recieves signal and performs actions.
from .models import Profile#because we are creating profile in our function.


@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
#if there is a user that is saved then send it to receiver.The receiver will take the 4 argumets that it gets
#and if the user is created(the condition in if statement) then n instance of the user as a profile is created.
@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
#the above saves a profile of a user that is created.