from django.urls import path, URLPattern, URLResolver
from api import views


app_name= 'api'

urlpatterns = [
    path('api/hello/',views.HelloAPIView.as_view(),name='hello'),
    path('api/counters',views.CounterListView.as_view(),name='counter_list_serialize'),
    path('api/counters/<pk>/',views.CounterDetailView.as_view(),name='counter_detail_serialize'),
    path('api/increase/<pk>/',views.CounterIncreaseView.as_view(),name='counter_increase'),
    path('api/decrease/<pk>/',views.CounterDecreaseView.as_view(),name='counter_decrease'),
    path('api/new_counter/',views.NewCounter.as_view(),name='new_counter'),
]