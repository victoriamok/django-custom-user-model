from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserChangeForm, UserAuthenticationForm


# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


@login_required
def home(request):
    return render(request, 'home.html')


def registration_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password2')
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(response):
    logout(response)
    return redirect('home')


def login_view(response):
    user = response.user
    if user.is_authenticated:
        return redirect('home')

    if response.method == 'POST':
        form = UserAuthenticationForm(response.POST)
        if form.is_valid():
            email = response.POST['email']
            password = response.POST['password']
            user = authenticate(
                email=email,
                password=password
            )

            if user:
                login(response, user)
                return redirect('home')
    else:
        form = UserAuthenticationForm()

    return render(response, 'registration/login.html', {'form': form})
