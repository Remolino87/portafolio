from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True, label='Nombre')
    email = forms.EmailField(required=True, label='Correo Electrónico')
    mensaje = forms.CharField(widget=forms.Textarea, required=True, label='Mensaje')

    # Validación personalizada para el email (puedes ajustar las reglas a tus necesidades)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('Solo aceptamos correos de Gmail.')
        return email
