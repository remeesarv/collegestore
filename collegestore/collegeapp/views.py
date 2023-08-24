from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
app_name='collegeapp'

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['conpassword']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username exists")
                return redirect('collegeapp:register')
            else:
                user = User.objects.create_user(username=username,password=password)
                messages.info(request, "user created")
                user.save()
                return redirect('collegeapp:login')
        else:
            messages.error(request, "Password not match")
            return redirect('collegeapp:register')
        return redirect('/')
    return render(request, "register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,"button.html")
        else:
            messages.error(request, "Invalid credential")
            return redirect('collegeapp:login')
    return render(request, "login.html")
def registration(request):
    return render(request,"form.html")
def submit(request):
        return render(request,"submit.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
