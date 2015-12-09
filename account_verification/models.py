from authy import AuthyApiException
from authy.api import AuthyApiClient
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    """Our user model. Extends Django's AbstractUser model"""
    phone_number = PhoneNumberField(blank=True)
    authy_id = models.CharField(max_length=50, blank=True, verbose_name='Authy ID')

    def send_verification_token(self):
        """
        Creates an Authy user if one does not yet exist, and then sends
        a verification token
        """
        authy_client = AuthyApiClient(settings.AUTHY_API_KEY)
        
        if not self.authy_id:
            authy_user = authy_client.users.create(
            self.email,
            self.phone_number.national_number,
            self.phone_number.country_code)

            if authy_user.ok():
                self.authy_id = authy_user.id
                self.save()
            else:
                raise AuthyApiException()

        # Send a verification token to the user, forcing delivery via SMS
        # even if the user has the Authy app installed on their phone
        token_request = authy_client.users.request_sms(
            self.authy_id,
            {'force': True})

        if not token_request.ok():
            raise AuthyApiException()
