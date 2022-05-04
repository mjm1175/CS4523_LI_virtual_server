from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

# not required, just to display/search/edit
class AccountAdmin(UserAdmin):
#	list_display = ('email', 'username', 'role', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('email', 'username')
	read_only = ('date_joined', 'last_login', 'slug', 'uniqueId')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Experience)
