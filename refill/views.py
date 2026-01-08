from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicineDetails, Notification
from .forms import MedicineDetailsforms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User

# Create your views here.


@login_required
def home(request):
    medicines = MedicineDetails.objects.filter(user=request.user)
    notifications = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).order_by('-created_at')

    if request.method == "POST":
        form = MedicineDetailsforms(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)   
            medicine.user = request.user          
            medicine.save()
            return redirect('home')
    else:
        form = MedicineDetailsforms()

    return render(request, 'add.html', {
        'obj': medicines,
        'notifications': notifications,
        'form': form
    })

@login_required
def edit(request, id):
    medicine = get_object_or_404(MedicineDetails, id=id, user=request.user)
    if request.method == "POST":
       form = MedicineDetailsforms(request.POST, instance=medicine)
       if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = MedicineDetailsforms(instance=medicine)
    obj = MedicineDetails.objects.filter(user=request.user)
    return render(request, 'add.html', {
        'form':form,
        'obj': obj,
        'edit_item': medicine
    })



@login_required
def delete(request, id):
    obj = get_object_or_404(MedicineDetails, id=id, user = request.user)
    obj.delete()
    return redirect('home')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username = username).exists():
            return render(request, "register.html", {"error":"Username already exists"})
        
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
        login(request, user)
        return redirect("home")
    
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username , password=password)
        
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("home")
        else:
            return render(request, "login.html",{"error":"Invalid Credentials"})
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
