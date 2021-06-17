# app_detalle
import json
from django.shortcuts import render, redirect, get_object_or_404 #
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

import random
import csv
from django.contrib import messages #
from django.contrib.messages.views import SuccessMessageMixin #
from functools import wraps
from urllib.parse import urlparse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.shortcuts import reverse, redirect #
from django.utils.http import urlencode
from django import forms #

#---------------------------------------------#
#from .forms import  CustomUserCreationForm (sólo si esta creado en el forms.py)

from .models import Entradas #


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #
from django.views.generic import TemplateView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView #


# Create your views here.
# app_entradas #

#def index(request):
#    return render(request,'app_categorias/index.html')

class EntradasListView(ListView) :
    model = Entradas
    template_name = 'app_entradas/index.html'

class Create_Entradas(TemplateView) :
    template_name = 'app_entradas/crear.html'