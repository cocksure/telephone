from django import forms
from .models import MyTable


class MyTableForm(forms.ModelForm):
    class Meta:
        model = MyTable
        fields = ('department', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10')
