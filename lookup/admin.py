from django.contrib import admin

from lookup.models import *

# Register your models here.
admin.site.register(StaffRoleLookup)
admin.site.register(MemberRoleLookup)
admin.site.register(LocationLookup)
admin.site.register(HealthFacilityLookup)
admin.site.register(ProjectLevelLookup)