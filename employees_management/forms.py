from django import forms
from django.forms import inlineformset_factory
from .models import Employee, Address, Contact, Document

# Employee form
class EmployeeForm(forms.ModelForm):
    birthday = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',  # HTML5 date input
                'class': 'form-control',  # Optional: You can add any CSS class for styling
                'placeholder': 'Select a date'
            }
        )
    )
    class Meta:
        model = Employee
        fields = ['code', 'name', 'birthday', 'remarks']

# Address Form
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_type', 'country', 'city', 'remarks']

# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_type', 'value']

# Document Form
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'file_description', 'remarks']

# Define formsets for Address, Contact, and Document linked to Employee
AddressFormSet = inlineformset_factory(
    Employee, Address, form=AddressForm, extra=1, can_delete=True
)

ContactFormSet = inlineformset_factory(
    Employee, Contact, form=ContactForm, extra=1, can_delete=True
)

DocumentFormSet = inlineformset_factory(
    Employee, Document, form=DocumentForm, extra=1, can_delete=True
)
