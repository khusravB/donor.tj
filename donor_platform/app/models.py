from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime, os


class CustomUser(AbstractUser):
    ROLES = [
        ('donor', 'Donor'),
        ('organization', 'Organization'),
    ]
    role = models.CharField(max_length=30, choices=ROLES, default='organization')
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        app_label = 'app'


class Organization(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class DonorHistory(models.Model):
    volume_of_all_donations = models.DecimalField(max_digits=5, decimal_places=2)


class Donor(models.Model):
    TYPES_OF_BLOOD = [
        ('First Positive', 'O(I) Rh+'),
        ('First Negative', 'O(I) Rh−'),
        ('Second Positive', 'A(II) Rh+'),
        ('Second Negative', 'A(II) Rh−'),
        ('Third Positive', 'B(III) Rh+'),
        ('Third Negative', 'B(III) Rh-'),
        ('Fourth Positive', 'AB(IV) Rh+'),
        ('Fourth Negative', 'AB(IV) Rh-'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_info = models.TextField(null=True, blank=True)
    blood_type = models.CharField(max_length=50, choices=TYPES_OF_BLOOD, default='First Positive', null=True, blank=True)
    donor_history = models.ForeignKey(DonorHistory, on_delete=models.CASCADE, null=True, blank=True)


class DonationApplication(models.Model):
    TYPES_OF_BLOOD = [
        ('First Positive', 'O(I) Rh+'),
        ('First Negative', 'O(I) Rh−'),
        ('Second Positive', 'A(II) Rh+'),
        ('Second Negative', 'A(II) Rh−'),
        ('Third Positive', 'B(III) Rh+'),
        ('Third Negative', 'B(III) Rh-'),
        ('Fourth Positive', 'AB(IV) Rh+'),
        ('Fourth Negative', 'AB(IV) Rh-'),
    ]

    needing_person = models.CharField(max_length=255)
    organization = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                     related_name='donation_applications_as_organization')
    requested_amount_liters = models.DecimalField(max_digits=5, decimal_places=2)
    requested_amount_quantity = models.PositiveIntegerField()
    received_amount_quantity = models.PositiveIntegerField(null=True, blank=True)
    received_amount_liters = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    blood_type = models.CharField(max_length=50, choices=TYPES_OF_BLOOD, default='First Positive')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    all_donors = models.ManyToManyField(CustomUser, related_name='donation_applications_as_donor', blank=True)




