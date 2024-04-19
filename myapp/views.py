from django.shortcuts import render
from .forms import WeightInputForm
from .utils import calculate_days_to_target,calculate_maintenance_calories
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.shortcuts import  redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth import logout
from django.urls import reverse
from .models import Profile,WeightInput
from datetime import datetime, timedelta
from django.http import HttpResponse


def calculate_days_view(request):
    if request.method == 'POST':
        form = WeightInputForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            weight_input = form.save()

            # Calculate BMR and TDEE using the saved data
            bmr, tdee = calculate_maintenance_calories(weight_input.weight_kg, weight_input.height_cm, weight_input.age, weight_input.gender, weight_input.activity_level)

            # Calculate calories to be consumed per day for different weight loss options
            mild_weight_loss = tdee - (7700 * 0.25 / 7)
            moderate_weight_loss = tdee - (7700 * 0.5 / 7)
            extreme_weight_loss = tdee - (7700 * 1 / 7)

            # Redirect to target_weight view with weight_input_id
            return redirect(reverse('target_weight', kwargs={'weight_input_id': weight_input.id}))
    else:
        form = WeightInputForm()

    return render(request, 'calculate_days.html', {'form': form})




def home(request):
    user_profile = request.user.profile if request.user.is_authenticated and hasattr(request.user, 'profile') else None
    return render(request, 'home.html', {'user_profile': user_profile});

@login_required
def edit_profile(request):
    # Check if the user has a profile
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
    else:
        # If the profile doesn't exist, create a new one
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})


class SignUpView(View):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})

def custom_logout(request):
    if request.method == 'POST':
        # Custom logic before logging out (if needed)
        # ...

        # Perform the logout
        logout(request)

        # Redirect to a specific URL after logout (you can customize this)
        return redirect(reverse('home'))
    else:
        # If the request is not a POST request, you can handle it accordingly
        return render(request, 'registration/logout.html', {'error_message': 'Invalid request method'})


def target_weight_view(request, weight_input_id):
    # Retrieve the WeightInput instance using the provided weight_input_id
    try:
        weight_input = WeightInput.objects.get(id=weight_input_id)
    except WeightInput.DoesNotExist:
        return render(request, 'error.html', {'message': 'WeightInput not found'})

    # Use the calculation logic from utils.py
    result = calculate_days_to_target(weight_input.current_weight, weight_input.target_weight, weight_input.strategy)

    return render(request, 'target_weight.html', {'weight_input': weight_input, 'result': result})