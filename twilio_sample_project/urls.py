from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Your URLs go here
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^account/', include('account_verification.urls')),

    # Include the Django admin
    url(r'^admin/', include(admin.site.urls)),
]
