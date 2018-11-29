from api.models import (
    Address, Property,
    State, ZillowInformation)

from rest_framework import serializers


class StateListSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('name', 'abbreviation')


class AddressListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'line1', 'line2', 'city', 'state', 'postal_code')


class ZillowInformationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZillowInformation
        fields = (
            'zillow_id', 'link',
            'rent_est', 'rent_est_last_updated',
            'price_est', 'price_est_last_updated')


class PropertyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = (
            'area_unit', 'bathrooms', 'bedrooms',
            'home_size', 'home_type', 'price',
            'area_unit', 'bathrooms', 'bedrooms',
            'price_last_sold', 'date_last_sold',
            'rent', 'property_size', 'tax_value',
            'tax_year', 'year_built',
            'address', 'zillow')
