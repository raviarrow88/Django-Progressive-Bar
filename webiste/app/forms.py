from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator

class CreateUserForm(forms.Form):
    total = forms.IntegerField(
    validators=[
    MinValueValidator(5),
    MaxValueValidator(500)
        ]
    )
