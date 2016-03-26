from django import forms

from .models import Guest
from .models import Enquiry,Requirement,DatabaseInsert


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('first_name','phone_number',)

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('need',)

class RequirementForm(forms.ModelForm):
    class meta:
        model = Requirement
        fields =('query',)

class DatabaseForm(forms.ModelForm):
    class meta:
        model = DatabaseInsert
        fields = ('username','phone',)
    
