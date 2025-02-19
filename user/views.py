from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User


def login_page(request):
    print(request.POST.get('username'))
    print(request.POST.get('password'))
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/user-api/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/user-api/login/')
        else:
            login(request, user)
            return redirect('/country-api/all-country/')

    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/user-api/login/')

        user = User.objects.create_user(
            username=username
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully!")
        return redirect('/user-api/login/')

    return render(request, 'register.html')

