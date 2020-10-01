from django.contrib.auth import (
    authenticate,
    login,
    logout,

)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    UserAuthenticationForm,
    RemoveUser,
    UserAccountUpdateForm,
)


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
            password = form.cleaned_data.get('password2')
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.method == 'POST':
        form = UserAccountUpdateForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST.get('email'),
                "first_name": request.POST.get('first_name'),
                "last_name": request.POST.get('last_name'),
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = UserAccountUpdateForm(
            initial={
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }
        )

    context['account_form'] = form

    return render(request, "account.html", context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(
                email=email,
                password=password
            )
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def remove_user_view(request):
    if request.method == 'POST':
        form = RemoveUser(request.POST)
        if form.is_valid():
            user = request.user
            if user is not None:
                user.delete()
                messages.success(request, 'Profile successfully deleted.')
                return redirect('home')
    else:
        form = RemoveUser()
    return render(request, 'delete_account.html', {'form': form})
