from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponse
#from django.core.context_processors import csrf
from regandauth.forms import (
    RegistrationForm,
    #EditProfileForm
)
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = auth.authenticate(
                request,
                username = username,
                password = password
            )
            return redirect('/')
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'regandauth/register.html', args)

