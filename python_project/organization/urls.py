from django.urls import path
from .views import OrganizationListCreateView, OrganizationDetailView, OrganizationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('organization', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organization/<int:pk>', OrganizationDetailView.as_view(), name='organization-detail'),
    path('organization-crud', OrganizationView.as_view(), name='organization'),
    path('organization-crud/<int:pk>', OrganizationView.as_view(), name='organization-id'),
    path('api/token/', obtain_auth_token, name='api-token'),


    # Add more URLs as needed
]