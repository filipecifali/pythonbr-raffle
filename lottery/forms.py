from django.forms import ModelForm
from lottery.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
