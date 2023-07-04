from django.shortcuts import render
from .forms import Register
from .models import UserData
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Adding the salt to password
        salt = bcrypt.gensalt()
         
        # Hash the password and store all details to the database
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Printing the salt
        print("Salt:")
        print(salt)
 
        # Printing the hashed
        print("Hashed:")
        print(hashed)

        # Storing the details to the database
        user = UserData(username=username, email=email, password=hashed)
        user.save()

        context = {
            'email': email,
            'username': username,
            'password': hashed
        }

        return render(request, 'register.html', context)

    return render(request, 'register.html')
