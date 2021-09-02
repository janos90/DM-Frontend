from django.forms import ModelForm, TextInput, Select, NumberInput, DateInput, SelectMultiple

from dogmeets.models import Dog, Activity


class DateInput(DateInput):
    input_type = 'date'


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'breed', 'height', 'weight', 'birthday', 'owner', 'image')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'breed': TextInput(attrs={'class': 'form-control'}),
            'height': NumberInput(attrs={'class': 'form-control'}),
            'weight': NumberInput(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control'}),
            'owner': Select(attrs={'class': 'form-control'})
        }


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'startTime', 'location', 'users', 'dogs')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'location': TextInput(attrs={'class': 'form-control'}),
            'users': SelectMultiple(attrs={'class': 'form-control'}),
            'dogs': SelectMultiple(attrs={'class': 'form-control'}),
            'startTime': DateInput(attrs={'class': 'form-control'})
        }
