from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Title'}),
    )
    subtitle = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Subtitle'}),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Description', 'id': 'summernote'}),
    )
    amount = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Amount'}),
    )
    status_text = forms.ChoiceField(
        choices=[('Enable', 'Enable'), ('Disable', 'Disable')],
        widget=forms.Select(
            attrs={'class': 'form-control select2', 'data-placeholder': 'Status'}),
        label='Status'
    )
