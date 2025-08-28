from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate

def register_account(request):
    responce = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            responce = HttpResponseRedirect(redirect_to=reverse("app_counter:index"))
        else:
            responce= render(request=request,template_name="register_app/register_account.html",context={'form': form})
    else:
        form = UserCreationForm()
        responce = render(request=request,template_name='register_app/register_account.html',context={'form': form})
    return responce