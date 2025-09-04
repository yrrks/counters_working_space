from django.urls import path, URLPattern, URLResolver
from api import views
from settings.urls import urlpatterns

app_name= 'api'

urlpatterns = [
    path('api/hello/',views.HelloAPIView.as_view(),name='hello'),
]