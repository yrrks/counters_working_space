from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import UserTheme

@login_required
def change_theme(request, theme_name):
    if theme_name in ['white','dark']:
        UserTheme.objects.update_or_create(
            user=request.user,
            defaults={'theme': theme_name}
        )

    return redirect(request.META.get('HTTP_REFERER','/'))
