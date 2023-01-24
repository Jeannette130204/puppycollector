from django.forms import ModelForm
from .models import Walkings

class WalkingsForm(ModelForm):
    class Meta:
        model = Walkings
        fields = ['date', 'walk']