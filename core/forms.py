from django import forms
from core.models import aluno

class StudentForm(forms.ModelForm):
    class Meta:
        model = aluno
        fields = '__all__'