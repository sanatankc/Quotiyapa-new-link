from django.forms import ModelForm

from .models import Quotes

class Quotes_form(ModelForm):
    """
    Form to add Quotes
    """
    class Meta:
        model = Quotes
        fields = ('quotes', 'author')