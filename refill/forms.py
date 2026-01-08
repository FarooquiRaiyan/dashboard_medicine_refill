from django import forms
from .models import MedicineDetails

class MedicineDetailsforms(forms.ModelForm):
    class Meta :
        model = MedicineDetails
        exclude = ('user',)
        widgets= {
            'med_name': forms.TextInput(attrs={'placeholder':'Medicine Name'}),
            'med_user':forms.TextInput(attrs={'placeholder':'Patient Name'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            
        }
        start_date = forms.DateField(
            widget = forms.DateInput(
                attrs ={
                    'type':'data',
                    'class':'form-control'
                }
            )
        )
        
        