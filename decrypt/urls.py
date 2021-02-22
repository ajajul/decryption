from django.urls import path
from decrypt import views

app_name = 'decrypt'

urlpatterns = [
    path('encryptMessage', views.encryptMessage.as_view(), name='encrypt-msg'),
    path('decryptMessage', views.DecryptMessage.as_view(), name='decrypt-msg'),
]
