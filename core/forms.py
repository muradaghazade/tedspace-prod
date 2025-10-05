from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'surname', 'email', 'position', 'company', 'country', 'message', ]
        widgets = {
            'name':forms.TextInput(attrs={'class':'input_small alishka'}),
            'surname':forms.TextInput(attrs={'class':'input_small alishka2'}),
            'email':forms.TextInput(attrs={'class':'input_medium',}),
            'position':forms.TextInput(attrs={'class':'input_medium',}),
            'company':forms.TextInput(attrs={'class':'input_medium',}),
            'country':forms.TextInput(attrs={'class':'input_medium',}),
            'message':forms.Textarea(attrs={'class':'input_large', 'rows': 4}),     
    }
        
        