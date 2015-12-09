from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class VerifiedUserAdmin(UserAdmin):
    """Extends the abstract Django user admin class, adding our extra fields"""

    def __init__(self, *args, **kwargs):
        super(VerifiedUserAdmin, self).__init__(*args, **kwargs)
        self.fieldsets[1][1]['fields'] += ('phone_number', 'authy_id')

admin.site.register(User, VerifiedUserAdmin)
