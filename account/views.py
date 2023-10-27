from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate


class RegistrationView(CreateView):
    template_name = 'account/signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            self.user = form.get_user()
            login(self.request, self.user)
            return redirect(self.get_success_url())

        context = self.get_context_data(form=form)
        context['login_error'] = "Invalid username"
        return render(self.request, self.template_name, context)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['login_error'] = "Invalid username or password"
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = 'login' 
