from django.contrib.auth import login
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required

User = get_user_model()

def index(request):
    if request.user.is_authenticated:
        try:
            records = Record.objects.filter(member=request.user) 
        except Record.DoesNotExist:
            records = []
    else:
        records = []  # 未登入為無記錄
    
    return render(request, 'index.html', {'records': records})

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
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

#record
@login_required  # 確保只有登入用戶才能訪問此視圖
def record_input(request):
    if request.method == 'POST':
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            record = record_form.save(commit=False)  # 先保存但不提交
            record.member = request.user  # 設置當前用戶為該交易的會員
            record.save()  # 提交並保存交易記錄
            return redirect('index')  # 提交後重定向回首頁

    else:
        record_form = RecordForm()

    categories = Category.objects.all()  # 確保載入所有分類
    category_form = CategoryForm()

    records = Record.objects.filter(member=request.user)

    return render(request, 'record_input.html', {
        'record_form': record_form,
        'category_form': category_form,
        'categories': categories,
        'records': records,  
    })


#管理分類
def category_management(request):
    categories = Category.objects.all()  # 確保獲取所有分類
    
    category_form = CategoryForm()

    for category in categories:
        print(category.category_ids)

    return render(request, 'category_management.html', {
        'categories': categories,
        'category_form': category_form,
    })

 