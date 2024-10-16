from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("all good")
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        print("not good")
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
@login_required
def profile_view(request):
    user = request.user
    if user.role == 'student':
        # Вернуть шаблон для студента
        return render(request, 'student.html', {'user': user})
    elif user.role == 'teacher':
        # Вернуть шаблон для учителя
        return render(request, 'teacher_profile.html', {'user': user})


