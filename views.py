from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout

def login_view(request):
  if request.method == 'POST':
    username =request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('home')
    return render(request,'index.html')
  
def logout_view(request):
    logout(request)
    return redirect('login') 
