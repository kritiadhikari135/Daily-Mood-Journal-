from django import forms
from .models import MoodEntry

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood', 'notes']
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'How are you feeling today?'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mood'].label = "Mood"
        self.fields['notes'].label = "Notes"
        self.fields['mood'].empty_label = "Select your mood"
        self.fields['notes'].widget.attrs['style'] = 'resize:vertical;'
