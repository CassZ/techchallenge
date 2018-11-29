from django.conf.urls import url

from rest_framework.documentation import include_docs_urls
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    AddressCreateListView, AddressDetailsView,
    PropertyCreateListView, PropertyDetailsView,
    StateCreateListView, StateDetailsView,
    ZillowInformationCreateListView, ZillowInformationDetailsView,)


urlpatterns = {
    url(r'^states/(?P<pk>[0-9]+)/$',
        StateDetailsView.as_view(),
        name="state-detail"),
    url(r'^states/$',
        StateCreateListView.as_view(),
        name="state-create-list"),
    url(r'^addresses/(?P<pk>[0-9]+)/$',
        AddressDetailsView.as_view(),
        name="address-detail"),
    url(r'^addresses/$',
        AddressCreateListView.as_view(),
        name="address-create-list"),
    url(r'^zillowinformation/(?P<pk>[0-9]+)/$',
        ZillowInformationDetailsView.as_view(),
        name="zillowinformation-detail"),
    url(r'^zillowinformation/$',
        ZillowInformationCreateListView.as_view(),
        name="zillowinformation-create-list"),
    url(r'^properties/(?P<pk>[0-9]+)/$',
        PropertyDetailsView.as_view(),
        name="property-detail"),
    url(r'^properties/$',
        PropertyCreateListView.as_view(),
        name="property-create-list"),
    url(r'^docs/', include_docs_urls(title='Technical Challenge'))
}

urlpatterns = format_suffix_patterns(urlpatterns)
