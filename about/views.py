from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

def about_me(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")

    about_instance = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    return render(
        request,
        "about/about.html",
        {
            "about": about_instance,
            "collaborate_form": collaborate_form,
        },
    )