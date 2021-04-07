from django.contrib import admin
from .models import Snippet
from django.contrib.auth.models import Group

from .models import Todo_user

# Register your models here.

admin.site.register(Todo_user)
admin.site.register(Snippet)
admin.site.unregister(Group)
admin.site.site_header='Admin Dashboard'