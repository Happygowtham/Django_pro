from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member 
import hashlib
  
def index(request):
    if request.method == 'POST':
    	passw=request.POST['password']
    	result = hashlib.md5(passw.encode())
    	password=result.hexdigest()
    	
    	member = Member(username=request.POST['username'], password=password,  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    	if Member.objects.filter(username=request.POST['username']).exists():
        	context = {'msg': 'Username already taken'}	
        	return render(request,"index.html",context)
    	else:      
	        member.save()
        	context = {'msg': 'Registered Succesfully'}	
        	return render(request,"login.html",context)
    else:
        return render(request, 'index.html')
 
def login(request):
    return render(request, 'login.html')
	
'''def setsession(request):  
	request.session['username'] = Member(username=request.POST['username'])
	request.session['password'] = password=password 
	return HttpResponse("session is set")    
'''
def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            global member
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)
    else:
    	if member:
    		return render(request, 'home.html', {'member': member})
    	else:      
    		return render(request, 'login.html')

def logout(request):
		return render(request, 'login.html')