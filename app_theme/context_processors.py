from .models import UserTheme

def theme_context(request):
    theme = 'white'

    if request.user.is_authenticated:

        user_theme,created = UserTheme.objects.get_or_create(user=request.user,defaults={'theme': 'white'})
        theme = user_theme.theme


    return { 'user_theme': theme }