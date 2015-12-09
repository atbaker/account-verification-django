from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegisterForm
from .models import User

def register_user(request):
    """Powers the new user sign up form"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            # Create the user
            user = User.objects.create_user(
                username=data['email'],
                email=data['email'],
                password=data['password1'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                phone_number=data['phone_number'])

            # Set the user id in the session
            request.session['user_id'] = user.id

            # Hang out here for now
            user.send_verification_token()

            messages.add_message(request, messages.INFO, 'Hello world.')
            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
