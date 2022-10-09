from django import forms
from quote.models import Quote
import datetime

class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = '__all__'
    