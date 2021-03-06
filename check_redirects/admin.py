from django.contrib import admin

from .models import Urllist, Responsetime
# Register your models here.

@admin.register(Urllist)
class url_list_admin(admin.ModelAdmin):
	list_display = ('site_url', 'target_url', 'enable', 'broken_redirect', 'actual_target')

@admin.register(Responsetime)
class response_time_admin(admin.ModelAdmin):
	list_display = ('id', 'response_time')
