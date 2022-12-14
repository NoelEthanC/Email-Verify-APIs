from django.urls import path
from . import views


urlpatterns = [
    path('', views.SignUp.as_view() , name='signup' ),
    path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
    
]