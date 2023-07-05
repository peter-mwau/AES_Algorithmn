import bcrypt
from django.shortcuts import render
from django.contrib import messages
from .models import UserData

# ...

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirmpassword')

        # Check if the passwords match
        if password != confirmpass:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        # Check if the username is already taken
        if UserData.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'register.html')

        # Check if the email is already taken
        if UserData.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken.')
            return render(request, 'register.html')

        # Generate a new salt
        salt = bcrypt.gensalt()

        # Hash the password with the generated salt
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Convert the hashed password and salt to strings
        hashed_str = hashed.decode('utf-8')
        salt_str = salt.decode('utf-8')

        # Storing the details to the database
        user = UserData(username=username, email=email, password=hashed_str, salt=salt_str)
        user.save()

        context = {
            'email': email,
            'username': username,
            'password': hashed_str, 
            'error': messages.error,
        }

        return render(request, 'login.html', context)

    return render(request, 'register.html')


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Retrieve user data from the database
            user = UserData.objects.get(username=username)
            hashed_password = user.password.encode('utf-8')
            salt = user.salt.encode('utf-8')

            # Concatenate the salt and the hashed password
            hashed_input_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            # Compare the concatenated passwords
            if hashed_password == hashed_input_password:
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
