from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import logout as auth_logout
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, "Passwords don't match. Please recheck and try again.")
            return render(request, 'users/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'users/register.html')

        user = User.objects.create_user(
            username=email,  
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, 'Account created. Please log in.')
        return redirect('login')  

    return render(request, 'users/register.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('homepage')  # Redirect to homepage after login
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, 'users/login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout
