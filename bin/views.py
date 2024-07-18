from django.shortcuts import render
from django.http import HttpResponse

from .models import Note


def index(request):
    return HttpResponse("Hello, world. You're at the")


def show_note(request, link):
    if not Note.objects.filter(link=link).exists():
        return HttpResponse(f"Note \"{link}\" doest not exist. 404")
    note = Note.objects.get(link=link)
    note.incr_click()
    note.save()

    context = {"text": note.note, "md_support": note.md_support}
    return render(request, "bin/bin.html", context)
