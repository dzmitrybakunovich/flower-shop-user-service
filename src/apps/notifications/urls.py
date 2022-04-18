from django.urls import path

from .views import NotifyView

urlpatterns = [
    path('send/', NotifyView.as_view(), name='send-notification'),
]
