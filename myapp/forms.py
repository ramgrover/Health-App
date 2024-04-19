from django import forms
from .models import WeightInput
from .models import Profile

from django import forms
from .models import WeightInput

class WeightInputForm(forms.ModelForm):
    class Meta:
        model = WeightInput
        fields = ['age', 'gender', 'activity_level', 'weight_kg', 'height_cm', 'target_weight', 'current_weight', 'goal', 'strategy']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'gender', 'fitness_goals', 'medical_history']