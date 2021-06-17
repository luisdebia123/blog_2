
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

import random
import csv
from django.contrib import messages 
from functools import wraps
from urllib.parse import urlparse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.shortcuts import reverse, redirect
from django.utils.http import urlencode

#from .forms import  CustomUserCreationForm (sólo si esta creado en el forms.py)

#from .models import Actor, Pelicula (sólo si estan creados en el models.py)

# Create your views here.


def principal(request):
    return render(request,'app_blog_02/principal.html')
