from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def app(request):
    return render(request, template_name='app.html')


def fetch_data(request):
    return render(request, template_name='partials/static_table.html')


def submit_form(request):
    content = request.POST.get('message') or ''
    Message(content=content).save()
    context = Message.objects.values_list('content', flat=True)
    return render(request, context=dict(messages=context), template_name='partials/form.html')
