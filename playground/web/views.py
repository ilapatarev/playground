from django import forms
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from playground.web.models import Field


UserModel = get_user_model()



def first_page(request):
    return render(request, 'index.html')
class RegistrationForm(UserCreationForm):
    offerer = forms.BooleanField(required=False)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'offerer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text for the password fields
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  # Set username as email
        if commit:
            user.save()
        return user

class UserRegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'profile/registration.html'
    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        username = form.cleaned_data['email']
        if get_user_model().objects.filter(username=username).exists():
            form.add_error('email', 'This email is already registered.')
            return self.form_invalid(form)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'profile/login.html'
    success_url = reverse_lazy('fields')



class LogoutView(LogoutView):
    next_page = reverse_lazy('first_page')

class FieldListView(ListView):
    model = Field
    template_name = 'field/fields.html'  # Specify the path to your field list template
    context_object_name = 'fields'  # Specify the variable name in the template

class FieldView(ListView):
    model = Field
    template_name = 'field/field-details.html'  # Specify the path to your field list template
    context_object_name = 'field-detail'
# class FieldCreateView(CreateView):
#     model = Field
#     template_name = 'field/add-field.html'  # Specify the path to your field create template
#     fields = ['name']  # Specify the fields to be displayed in the create form
#     success_url = '/fields/'  # Specify the URL to redirect after successful creation

class FieldUpdateView(UpdateView):
    model = Field
    template_name = 'field/edit-field.html'  # Specify the path to your field update template
    fields = ['name']  # Specify the fields to be displayed in the update form
    success_url = '/fields/'  # Specify the URL to redirect after successful update

class FieldDeleteView(DeleteView):
    model = Field
    template_name = 'field/delete-field.html'  # Specify the path to your field delete template
    success_url = '/fields/'
