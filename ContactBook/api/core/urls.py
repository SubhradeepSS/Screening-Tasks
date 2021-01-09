from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('auth', include('rest_framework.urls')),

    path('', views.ContactsView.as_view()),
    path('<pk>', views.ContactView.as_view()),
    
    path('search/name/<name>', views.SearchNameView.as_view()),
    path('search/email/<email>', views.SearchEmailView.as_view()),
]
