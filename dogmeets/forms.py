from django.forms import ModelForm, TextInput, Select, Textarea, NumberInput, DateInput

from dogmeets.models import Dog


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'breed', 'height', 'weight', 'birthday', 'owner')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'breed': TextInput(attrs={'class': 'form-control'}),
            'height': NumberInput(attrs={'class': 'form-control'}),
            'weight': NumberInput(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control'}),
            'owner': Select(attrs={'class': 'form-control'})
        }