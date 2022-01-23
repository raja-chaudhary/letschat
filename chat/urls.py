from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]

htmx_urlpatterns = [
    path('<str:room_name>/check-messages/',
         views.check_messages, name='check-messages'),
]

urlpatterns += htmx_urlpatterns
