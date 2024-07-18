from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from bin.models import Note

import random


def random_link(l=8):
    alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    return "".join(random.choice(alphabet) for _ in range(l))


@csrf_protect
def index(request):
    return render(request, "mainpage/index.html")


@csrf_protect
def add(request):
    if request.method == "POST":
        # Add check if account exist
        # as_guest = True if "as_guest" in request.POST else False
        md_support = True if "md_support" in request.POST else False
        pass_support = True if "pass_support" in request.POST else False
        custom_link_support = True if "custom_link_support" in request.POST else False

        text = request.POST["text"] if "text" in request.POST else None
        link = request.POST["link"] if "link" in request.POST else None
        password = request.POST["password"] if "password" in request.POST else None

        ip = request.META['REMOTE_ADDR']

        registered = False

        if not registered:
            link = random_link()
            # While link exist regenerate link
            while Note.objects.filter(link=link).exists():
                link = random_link()

            note = Note(
                note=text,
                link=link,
                password=password,
                ip=ip,
                md_support=md_support,
                as_guest=True,
            )

            note.save()

        return redirect(f"/{link}")
    else:
        return HttpResponse("0")
