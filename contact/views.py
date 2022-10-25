from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForms

# Create your views here.
def contact(request):
    contact_form = ContactForms()

    if request.method == "POST":
        contact_form = ContactForms(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")

            # Enviamos el correo
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["pancholape1@gmail.com"],
                reply_to=[email],  # Esto es a quien le respondemos con el botón de responder
            )

            try:
                email.send()
                # Si sale bien redireccionamos a ok
                return redirect(reverse("contact") + "?ok")
            except:
                # Si falla redireccionamos a fail
                return redirect(reverse("contact") + "?fail")

    return render(request, "contact/contact.html", {"form": contact_form})
