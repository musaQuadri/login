from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth  
from django.contrib import messages
from .models import Feature
import pyrebase, urllib

config={
  "apiKey": "AIzaSyAAmB5GSmWvsxXtKWgRf4-P43fFMyBHIEY",
  "authDomain": "test-ce8a7.firebaseapp.com",
  "databaseURL": "https://test-ce8a7-default-rtdb.firebaseio.com",
  "projectId": "test-ce8a7",
  "storageBucket": "test-ce8a7.appspot.com",
  "messagingSenderId": "561839911481",
  "appId": "1:561839911481:web:4162c21315bec995a153e8"
}

firebase = pyrebase.initialize_app(config)
authe= firebase.auth()
database=firebase.database()
storage=firebase.storage()

# Create your views here.
def index(request):
    feature=Feature.objects.all()
    return render(request, 'index.html', {'features':feature})


def register(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Username = request.POST['Username']
        Password = request.POST['Password']
        Password2 = request.POST['Password2']

        if Password == Password2:
            if User.objects.filter(Email=Email).exists():
                messages.info(request, 'Email already exists')
                return redirect('registration')
            elif User.objects.filter(Username=Username).exists():
                messages.info(request, 'Username not available')
                return redirect('registration')
            else:
                user = User.objects.create_user(Username=Username, Email=Email, Password=Password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('registration')
    else:
        return render(request, 'registration.html' )


