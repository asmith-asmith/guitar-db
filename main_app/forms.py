from django.forms import ModelForm
from .models import Variations

class VariationsForm(ModelForm):
  class Meta:
    model = Variations
    fields = ['date_created', 'name']