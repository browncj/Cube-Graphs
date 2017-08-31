from django import forms

from about.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'response_email']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'response_email': forms.TextInput(attrs={'size': 60}),
        }
