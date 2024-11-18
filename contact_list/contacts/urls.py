"""
URL configuration for contact_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from .views import ContactListView, ContactDetailView, ContactCreateView, ContactUpdateView, ContactDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    #crud operations in api
    path('contacts/',ContactListView.as_view(),name = 'contact-list'),
    path('contacts-create/',ContactCreateView.as_view(),name = 'contact-create'),
    path('contacts/<int:pk>/',ContactDetailView.as_view(),name = 'contact-detail'),\
    path('contacts/<int:pk>/update/',ContactUpdateView.as_view(),name = 'contact-update'),
    path('contacts/<int:pk>/delete/',ContactDeleteView.as_view(),name = 'contact-delete'),


    #jwt token api
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name = 'token_refresh'),
]
