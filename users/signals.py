from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import Profile

# When user from User model is saved -> send signal 'post_save' to  -> receiver 'create_profile' will take the arguments 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwarks):
    if created:
        Profile.objects.create(user=instance)

# Save signal
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwarks):
        instance.profile.save()