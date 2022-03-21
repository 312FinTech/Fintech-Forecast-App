from django import forms
from .models import Prediction, Size

# class PredictionForm(forms.Form):
#     ticker = forms.CharField(label='Topping 1', max_length=100)
#     days = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])

class PredictionForm(forms.ModelForm):

    class Meta:
            model = Prediction
            fields = ['ticker', 'days', 'size']
            labels = {
            "ticker": "Ticker",
            "days": "Number of Days",
            }

class MultiplePredictionForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
