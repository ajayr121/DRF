from django.urls import path
from .views import (
    HelloView, UserRegisterView, UserListView, 
    UserDetailView, UserUpdateView, UserDeleteView
)

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('list/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('list/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('list/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
