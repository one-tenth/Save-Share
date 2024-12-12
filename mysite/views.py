from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PhoneForm
from django.contrib.auth import get_user_model
User = get_user_model()

def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']


            # 創建用戶
            user = User.objects.create_user(username=username, email=email, password=password,phone=phone)
            user.save()

            messages.success(request, "註冊成功！")
            return redirect('home')
        else:
            return render(request, 'accounts/register.html', {'form': form})

    # GET 請求
    form = PhoneForm()
    return render(request, 'accounts/register.html', {'form': form})



from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')