from django.conf.urls import url

from .views import register_user

urlpatterns = [
    # URLs for searching for and purchasing a new Twilio number
    url(r'^register$', register_user, name='register'),
]
