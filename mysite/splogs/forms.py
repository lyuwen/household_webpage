from splogs.models import Logs, Pmt
from django.forms import ModelForm
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class LogsForm(ModelForm):
    class Meta:
        model = Logs
        fields = ['date', 'name', 'product', 'price']
        widgets = { 'date': DateInput(), }

class PmtForm(ModelForm):
    class Meta:
        model = Pmt
        fields = ['date', 'fromN', 'toN', 'amount']
        widgets = { 'date': DateInput(), }
