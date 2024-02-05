from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))  # Utiliza un campo de entrada de fecha HTML5

    class Meta:
        model = Calificacion
        fields = ['nombre', 'nota', 'fecha']


class CalcularPromedioForm(forms.Form):
    fecha_parcial1_inicio = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Fecha de Inicio del Primer Parcial')
    fecha_parcial1_fin = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Fecha de Fin del Primer Parcial')
    fecha_parcial2_inicio = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Fecha de Inicio del Segundo Parcial')
    fecha_parcial2_fin = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Fecha de Fin del Segundo Parcial')