from django.contrib import admin
from tycoonConstruction.models import bidContractor, Projects, bidVendor, Estimation, VtoC_req

# Register your models here.
admin.site.site_header = "Tycoon Constructor admin"
admin.site.site_title = "Tycoon Constructor admin site"
admin.site.index_title = "Tycoon Constructor Admin"

admin.site.register(bidContractor)
admin.site.register(bidVendor)
admin.site.register(Estimation)
admin.site.register(VtoC_req)
admin.site.register(Projects)
