from django.urls import path
from decrypt import views

app_name = 'decrypt'

urlpatterns = [
    path('decryptMessage', views.DecryptMessage.as_view(), name='register'),
]
