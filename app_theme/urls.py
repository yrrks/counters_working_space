from django.urls import path
from . import views


app_name='app_theme'

urlpatterns = [
    path('theme/change/<str:theme_name>',views.change_theme,name='change_theme')
]