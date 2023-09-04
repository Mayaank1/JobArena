from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as login1,logout
from django.contrib import messages

from django.http import HttpResponse

def home(request):
    return render(request,'index(Homepage).html')
    #return HttpResponse("Hello")
def companies(request):
    return render(request,'Companies.html')
def login(request):
    return render(request,'login.html')
def support(request):
    return render(request,'support.html')
def hcl(request):
    return render(request,'hcl.html')
def deloitte(request):
    return render(request,'Deloitte.html')
def google(request):
    return render(request,'gooogle.html')
def ibm(request):
    return render(request,'ibm.html')
def intel(request):
    return render(request,'intel.html')
def jpmc(request):
    return render(request,'jpmc.html')
def template(request):
    return render(request,'template.html')
def meta(request):
    return render(request,'meta.html')
def microsoft(request):
    return render(request,'Microsoft.html')
def oracle(request):
    return render(request,'oracle.html')
def qualcomm(request):
    return render(request,'Qualcomm.html')
def salesforce(request):
    return render(request,'salesforce.html')
def tcs(request):
    return render(request,'tcs.html')
def accenture(request):
    return render(request,'accenture.html')
def amazon(request):
    return render(request,'Amazon.html')
def signup(request):
    return render(request,'signup.html')
def login_user(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        if len(username) < 5:
            messages.error(request,'Username must be at least 5 characters long.')
            return redirect('login')
        
        # Check password conditions
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return redirect('login')
        if not any(char.isdigit() for char in password):
            messages.error(request, 'Password must contain at least one digit.')
            return redirect('login')
        if not any(char.isupper() for char in password):
            messages.error(request, 'Password must contain at least one uppercase letter.')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login1(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')
    
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("You were logged out"))
    return redirect('home')
def details(request):
    return render(request,'json.html')
def submit_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')

        # Perform form validation
        if not name or not email or not phone or not comments:
            messages.error(request, 'All fields are required.')
            return redirect('contactus')  # Assuming 'contactus' is the URL name for the contact form page

        # Process the form data
        # ...

        # Retrieve form data from the request
        messages.success(request, 'Form submitted successfully.')


    # If the request method is not POST, render the form page
    return render(request, 'support.html')  # Replace 'contactus.html' with the actual template name