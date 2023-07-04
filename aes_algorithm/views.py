from django.shortcuts import render
from .forms import Register
from .models import UserData
import bcrypt

from django.shortcuts import render
from django.contrib import messages
from .models import UserData
import bcrypt

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Retrieve user data from the database
            user = UserData.objects.get(username=username)
            hashed_password = user.password

            # Compare the hashed passwords
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                # Redirect to homepage or perform necessary actions
                return render(request, 'homepage.html')
            else:
                # Passwords don't match
                messages.error(request, 'Invalid username or password.')
                return render(request, 'index.html')
        
        except UserData.DoesNotExist:
            # User data not found
            messages.error(request, 'Invalid username or password.')
            return render(request, 'index.html')

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
