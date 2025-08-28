from django.urls import path,include
from register_app import views


app_name = 'register_app'

urlpatterns= [
    path('register/', views.register_account, name='register'),
    path('', include('django.contrib.auth.urls')),

]