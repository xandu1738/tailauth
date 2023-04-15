from django.views.generic import CreateView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from.forms import SignUpForm

class ChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')

class UserRegistrationForm(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserEdit(UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('login')
    
    def get_object(self):
        return self.request.user
    
class Dashboard(TemplateView):
    template_name = 'dashboard.html'