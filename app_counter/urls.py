from django.urls import path
from app_counter import views

app_name='app_counter'

urlpatterns = [
    path("", views.index, name="index"),
    path("counter/",views.counter,name="counter"),
    path("counter/inc/<int:counter_id>",views.counter_inc,name="counter_inc"),
    path('counter/decr/<int:counter_id>',views.counter_decr,name='counter_decr'),
    path('counter/create',views.counter_create,name='counter_create'),
    path('counter/favorite/<int:counter_id>',views.choose_favorite,name='choose_favorite'),

]