from django.shortcuts import render
from rest_framework import generics
from .serializers import (
    StateListSerializer, AddressListSerializer,
    ZillowInformationListSerializer, PropertyListSerializer)
from .models import (
    State, Address,
    ZillowInformation, Property)
import django_filters.rest_framework


class StateDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class provides a Detail View of a State object.
    """
    queryset = State.objects.all()
    serializer_class = StateListSerializer


class StateCreateListView(generics.ListCreateAPIView):
    """
    This class allows creation and query of State objects.
    """
    queryset = State.objects.all()
    serializer_class = StateListSerializer
    filter_fields = ('name', 'abbreviation')

    def perform_create(self, serializer):
        serializer.save()


class AddressDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class provides a Detail View of an Address object.
    """
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer


class AddressCreateListView(generics.ListCreateAPIView):
    """
    This class allows creation and query of Address objects.
    """
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
    filter_fields = (
        'line1', 'line2', 'city', 'state', 'postal_code')

    def perform_create(self, serializer):
        serializer.save()


class ZillowInformationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class provides a Detail View of an 
    ZillowInformation object.
    """
    queryset = ZillowInformation.objects.all()
    serializer_class = ZillowInformationListSerializer


class ZillowInformationCreateListView(generics.ListCreateAPIView):
    """
    This class allows creation and query of 
    ZillowInformation objects.
    """
    queryset = ZillowInformation.objects.all()
    serializer_class = ZillowInformationListSerializer
    filter_fields = (
        'zillow_id', 'link',
        'rent_est', 'rent_est_last_updated',
        'price_est', 'price_est_last_updated')

    def perform_create(self, serializer):
        serializer.save()


class PropertyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class provides a Detail View of an Property object.
    """
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer


class PropertyCreateListView(generics.ListCreateAPIView):
    """
    This class allows creation and query of Property objects.
    """
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer
    filter_fields = (
        'area_unit', 'bathrooms', 'bedrooms',
        'home_size', 'home_type', 'price',
        'area_unit', 'bathrooms', 'bedrooms',
        'price_last_sold', 'date_last_sold',
        'rent', 'property_size', 'tax_value',
        'tax_year', 'year_built',
        'address', 'zillow')

    def perform_create(self, serializer):
        serializer.save()
