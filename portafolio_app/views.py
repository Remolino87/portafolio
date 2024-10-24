from django.shortcuts import render, redirect
from .forms import ContactForm 
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'portafolio_app/home.html')

def about(request):
    return render(request, 'portafolio_app/about.html')

def projects(request):
    return render(request, 'portafolio_app/projects.html')

from django.shortcuts import redirect

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Usa el formulario creado en forms.py
        if form.is_valid():
            # Aquí puedes procesar los datos del formulario
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # Puedes guardar los datos en la base de datos o enviarlos por email, etc.
            send_mail(
                f'Nuevo mensaje de {nombre}',
                f'Mensaje: {mensaje}\nEmail: {email}',
                'Bernardorecamalesgt@gmail.com',  # Desde este correo
                ['destinatario@correo.com'],  # A este correo
                fail_silently=False,
            )
            # Redirigir a una página de éxito
            return redirect('success')
    else:
        form = ContactForm()  # Si el método es GET, muestra un formulario vacío

    return render(request, 'portafolio_app/contact.html', {'form': form})

def success(request):
    return render(request, 'portafolio_app/success.html')