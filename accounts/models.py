from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
class User(AbstractUser):
    # date_of_birth = models.DateField()
    phone_number = models.IntegerField(blank=True,  null=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return({
            'refresh': str(refresh),
            'refresh': str(refresh.access_token),
        })
