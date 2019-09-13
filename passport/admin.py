from django.contrib import admin

# Register your models here.

# Register your models here.
from passport.models import UserGroup, User

admin.site.register(User)
admin.site.register(UserGroup)