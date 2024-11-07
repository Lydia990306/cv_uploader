from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import pandas as pd
from .forms import UserRegisterForm, CVUploadForm
from .models import CV
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile after registration
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    cv = CV.objects.filter(user=request.user).first()
    return render(request, 'users/profile.html', {'cv': cv})

@login_required
def upload_cv(request):
    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user

            # Process and store Excel file contents
            excel_file = request.FILES['uploaded_file']
            df = pd.read_excel(excel_file)
            cv.content = df.to_string()
            cv.save()
            return redirect('profile')
    else:
        form = CVUploadForm()
    return render(request, 'users/upload_cv.html', {'form': form})

@staff_member_required
def admin_view(request):
    cvs = CV.objects.all()
    return render(request, 'users/admin_view.html', {'cvs': cvs})
# views.py


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to profile after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
