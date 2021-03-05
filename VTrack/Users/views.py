from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}! Now you can login')
            return redirect('login')
    else:
        form = UserRegisterForm()
        p_form = ProfileUpdateForm()
    return render(request, 'Users/register.html', {'form': form, 'p_form': p_form })


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        form = PasswordChangeForm(request.user, request.POST)


        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile edited')
            return redirect('profile')


        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, f'Password changed for {username}!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        form = PasswordChangeForm(request.user)
    return render(request, 'Users/profile.html', {'form': form, 'u_form': u_form, 'p_form': p_form})

def app(request):
    return render(request, 'home/home.html')

