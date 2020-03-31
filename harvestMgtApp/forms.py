from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Plant

from .models import Farmer, FarmerGrows


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class AddFarmerForm(ModelForm):
    class Meta:
        model = Farmer
        fields = ['fName', 'nic', 'district']


class FarmerGrowsForm(ModelForm):
    class Meta:
        model = FarmerGrows
        fields = ['plant', 'farmer', 'amount']


class MyForm(forms.Form):

    all_plants = Plant.objects.all()

    INTEGER_CHOICES = [tuple([x, x]) for x in all_plants]
    original_field =  forms.CharField(label="What is today's date?", widget=forms.Select(choices=INTEGER_CHOICES))
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()