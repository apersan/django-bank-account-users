from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'iban')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs['size'] = 45
        self.fields['lastName'].widget.attrs['size'] = 45
        self.fields['iban'].widget.attrs['size'] = 35
