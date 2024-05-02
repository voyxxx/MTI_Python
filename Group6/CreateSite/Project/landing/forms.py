from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(label="Имя")
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea)