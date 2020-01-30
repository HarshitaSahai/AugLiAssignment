from django import forms 
from .models import *
  
class upload(forms.ModelForm): 
  
    class Meta: 
        model = uploadImage 
        fields = ['pic'] 