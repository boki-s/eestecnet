from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.forms import forms
from django.shortcuts import redirect, render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap
from gmapi.maps import Geocoder
from members.models import Member


def newsletter(request):
    try:
        validate_email( request.POST['mailsub'] )
    except ValidationError:
        return redirect("/")
    send_mail("Dear VC-IA, please kindly add "+request.POST['mailsub']+"to the newsletter list.",
              "eestecnet@gmail.com",
              "vc-ia@eestec.net")
    return redirect("/")


