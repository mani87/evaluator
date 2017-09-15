from django import forms

class AnswerForm(forms.Form):
	answer = forms.CharField(label="Your answer: ", required=True, widget=forms.Textarea)