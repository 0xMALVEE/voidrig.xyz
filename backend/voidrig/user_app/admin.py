from django.contrib import admin
from user_app.models import Invite

# Register your models here.
admin.site.register(Invite)

admin.site.site_title = "VOIDRIG"
admin.site.index_title = "VOIDRIG"
admin.site.site_header = "VOIDRIG ADMIN PANEL"