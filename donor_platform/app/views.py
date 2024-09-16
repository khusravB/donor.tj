from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins, status
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .models import *
from .serializers import *


class DonationApplicationViewSet(viewsets.ModelViewSet):
    queryset = DonationApplication.objects.all()
    serializer_class = DonationApplicationSerializer


class AddDonorView(APIView):
    def post(self, request, application_id, *args, **kwargs):
        user_id = request.user.id
        try:
            user = CustomUser.objects.get(id=user_id)
            applications = DonationApplication.objects.get(id=application_id)
            applications.all_donors.add(user)
            applications.save()

            return Response({'status': 'success', 'message': 'Donor added to donation application'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'status': 'error', 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except DonationApplication.DoesNotExist:
            return Response({'status': 'error', 'message': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
