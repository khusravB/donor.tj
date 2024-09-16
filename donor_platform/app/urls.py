from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from .views import *

applications = routers.DefaultRouter()
applications.register(r'application', DonationApplicationViewSet)


urlpatterns = [
    path('', include(applications.urls)),
    path('donation-application/<int:application_id>/add-donor/', AddDonorView.as_view(), name='add-donor'),

]
