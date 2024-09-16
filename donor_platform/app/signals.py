from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("Code is in this condition")
        if instance.role == 'donor':
            Donor.objects.create(user=instance)
        elif instance.role == 'organization':
            Organization.objects.create(user=instance)
