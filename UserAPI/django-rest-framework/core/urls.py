from django.urls import path, include

from .views import index, UsersView, UserView

urlpatterns = [
    path('', index, name='index'),
    path('users', UsersView.as_view(), name='users'),
    path('users/<int:user_id>', UserView.as_view(), name='user'),
]
