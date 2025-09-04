from django.contrib import admin
from django.urls import path, include
from app_counter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_counter.urls')),
    path('accounts/', include('register_app.urls')),
    path('',include('app_theme.urls')),
    path('',include('api.urls')),
]
