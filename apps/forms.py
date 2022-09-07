from .models import StudentDetail
from django import forms
import datetime


class SubjectForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = ("__all__")