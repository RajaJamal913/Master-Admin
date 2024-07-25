from django.contrib import admin
from .models import UserProfile,Order,BannedIP,ActivityLog,API
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(BannedIP)
admin.site.register(ActivityLog)
admin.site.register(API)