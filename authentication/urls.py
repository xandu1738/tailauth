from django.urls import path
from .views import UserRegistrationForm, UserEdit, ChangePassword,Dashboard
from . import views

urlpatterns = [
    path('register/', UserRegistrationForm.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='profile_edit'),
    path('password/', ChangePassword.as_view(template_name='registration/change_password.html'), name='password'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]

