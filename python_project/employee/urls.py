from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.EmployeeLogin.as_view(),name='login')


    # Add more URLs as needed
]