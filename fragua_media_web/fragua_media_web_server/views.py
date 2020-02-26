from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template,select_template,render_to_string


# Create your views here.

def index(request):
    return HttpResponse(render_to_string(template_name='index.html'))
